#!/usr/bin/env python
"""
GitLab订阅管理 - 运行端脚本

用于CI/CD流水线，基于GitLab MR的变更文件列表，查询哪些用户订阅了相关路径。

使用方法：
    python gitlab_runner.py <project_id> <changed_files_json> [target_branch]

参数说明：
    project_id       - 管理端的GitLab项目ID（整数）
    changed_files    - 变更文件路径的JSON数组字符串
    target_branch    - (可选) MR的目标分支，不提供则匹配所有分支

环境变量：
    BK_GITLAB_SUB_API_URL  - 管理端API地址（必填）
    BK_APP_CODE            - 蓝鲸应用ID（必填）
    BK_APP_SECRET          - 蓝鲸应用密钥（必填）
    RUNNER_TIMEOUT         - 请求超时秒数（默认30）

输出（JSON）：
    {
        "enterprise_username1": ["src/main.py", "src/utils.py"],
        "enterprise_username2": ["docs/README.md"]
    }
    key为企业用户名，value为该用户订阅路径内被变更的文件列表

示例（GitLab CI/CD）：
    stages:
      - notify

    notify-subscribers:
      stage: notify
      script:
        - |
          CHANGED_FILES=$(git diff --name-only $CI_MERGE_REQUEST_DIFF_BASE_SHA $CI_COMMIT_SHA | python3 -c "
          import sys, json; print(json.dumps(sys.stdin.read().strip().splitlines()))
          ")
          python3 runner/gitlab_runner.py $MANAGEMENT_PROJECT_ID "$CHANGED_FILES" $CI_MERGE_REQUEST_TARGET_BRANCH_NAME
      rules:
        - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
"""
import json
import logging
import os
import sys
from typing import Dict, List, Optional

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger(__name__)

# API endpoint path
CHANGES_ENDPOINT = "/api/runner/changes/"


def get_user_changes(
    api_base_url: str,
    app_code: str,
    app_secret: str,
    project_id: int,
    changed_files: List[str],
    target_branch: Optional[str] = None,
    timeout: int = 30,
) -> Dict[str, List[str]]:
    """
    调用管理端API，获取变更的用户映射。

    Args:
        api_base_url: 管理端API基础地址（例如 https://bk.example.com/o/bk_gitlab_sub）
        app_code: 蓝鲸应用ID
        app_secret: 蓝鲸应用密钥
        project_id: 管理端GitLab项目ID
        changed_files: 变更文件路径列表
        target_branch: MR目标分支（可选）
        timeout: 请求超时秒数

    Returns:
        dict: {enterprise_username: [changed_file_paths]}

    Raises:
        requests.HTTPError: API请求失败
        ValueError: 响应格式不符合预期
    """
    url = api_base_url.rstrip("/") + CHANGES_ENDPOINT
    headers = {
        "Content-Type": "application/json",
        "X-Bk-App-Code": app_code,
        "X-Bk-App-Secret": app_secret,
    }
    payload = {
        "project_id": project_id,
        "changed_files": changed_files,
    }
    if target_branch:
        payload["target_branch"] = target_branch

    logger.info(
        "Calling management API: project_id=%s, changed_files=%d, target_branch=%s",
        project_id,
        len(changed_files),
        target_branch or "all",
    )

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logger.error("API request timed out after %d seconds", timeout)
        raise
    except requests.exceptions.ConnectionError as e:
        logger.error("Cannot connect to management API at %s: %s", url, e)
        raise
    except requests.exceptions.HTTPError as e:
        logger.error("API returned error status %s: %s", response.status_code, response.text)
        raise

    try:
        result = response.json()
    except ValueError as e:
        logger.error("Invalid JSON response from API: %s", response.text[:200])
        raise ValueError(f"API returned invalid JSON: {e}") from e

    if not isinstance(result, dict):
        raise ValueError(f"Unexpected API response format: {type(result)}")

    if "result" in result and not result["result"]:
        error_msg = result.get("message", "Unknown error")
        raise ValueError(f"API returned error: {error_msg}")

    # Extract data from standard response envelope
    data = result.get("data", result)
    if not isinstance(data, dict):
        raise ValueError(f"Unexpected data format in API response: {type(data)}")

    logger.info("Successfully retrieved changes for %d users", len(data))
    return data


def main():
    """主函数，从命令行参数读取输入并调用API。"""
    if len(sys.argv) < 3:
        print(
            "Usage: python gitlab_runner.py <project_id> <changed_files_json> [target_branch]",
            file=sys.stderr,
        )
        print(
            "Example: python gitlab_runner.py 1 '[\"src/main.py\", \"docs/README.md\"]' main",
            file=sys.stderr,
        )
        print("\nEnvironment variables required:", file=sys.stderr)
        print("  BK_GITLAB_SUB_API_URL  - Management API base URL", file=sys.stderr)
        print("  BK_APP_CODE            - BlueKing app code", file=sys.stderr)
        print("  BK_APP_SECRET          - BlueKing app secret", file=sys.stderr)
        sys.exit(1)

    # Parse arguments
    try:
        project_id = int(sys.argv[1])
    except ValueError:
        print(f"ERROR: project_id must be an integer, got: {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    try:
        changed_files = json.loads(sys.argv[2])
        if not isinstance(changed_files, list):
            raise ValueError("changed_files must be a JSON array")
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR: Invalid changed_files JSON: {e}", file=sys.stderr)
        sys.exit(1)

    target_branch = sys.argv[3] if len(sys.argv) > 3 else None

    # Read configuration from environment variables
    api_base_url = os.environ.get("BK_GITLAB_SUB_API_URL", "").strip()
    app_code = os.environ.get("BK_APP_CODE", "").strip()
    app_secret = os.environ.get("BK_APP_SECRET", "").strip()
    timeout = int(os.environ.get("RUNNER_TIMEOUT", "30"))

    # Validate configuration
    missing_vars = []
    if not api_base_url:
        missing_vars.append("BK_GITLAB_SUB_API_URL")
    if not app_code:
        missing_vars.append("BK_APP_CODE")
    if not app_secret:
        missing_vars.append("BK_APP_SECRET")

    if missing_vars:
        print(f"ERROR: Missing required environment variables: {', '.join(missing_vars)}", file=sys.stderr)
        sys.exit(1)

    if not changed_files:
        # No files changed, output empty result
        print(json.dumps({}))
        sys.exit(0)

    try:
        result = get_user_changes(
            api_base_url=api_base_url,
            app_code=app_code,
            app_secret=app_secret,
            project_id=project_id,
            changed_files=changed_files,
            target_branch=target_branch,
            timeout=timeout,
        )
        # Output JSON result to stdout (for pipeline consumption)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        logger.error("Fatal error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
