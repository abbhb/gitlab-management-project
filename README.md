# GitLab订阅管理 (bk_gitlab_sub)

基于蓝鲸智云（BlueKing）开发框架构建的SaaS应用，用于管理GitLab项目中基于目录或文件变更的订阅通知。

## 项目介绍

当团队在GitLab上进行MR（Merge Request）时，本系统能够根据变更文件路径，自动识别订阅了相关目录/文件的用户，输出通知列表，方便流水线逐个触发通知。

## 核心功能

- **项目管理**：管理员注册GitLab项目到系统
- **订阅管理**：用户订阅感兴趣的目录或文件路径
- **变更匹配**：自动匹配变更文件与订阅路径
- **CI/CD集成**：提供运行端脚本，可集成到GitLab CI/CD流水线

## 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                     管理端 (SaaS)                        │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │ 蓝鲸登录  │  │ 权限中心  │  │    GitLab API集成     │  │
│  └──────────┘  └──────────┘  └──────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  项目管理 | 订阅管理 | 变更匹配 | REST API        │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ REST API
                           ▼
┌─────────────────────────────────────────────────────────┐
│                     运行端 (脚本)                         │
│  runner/gitlab_runner.py                                │
│  - 接收MR变更文件列表                                     │
│  - 调用管理端API查询订阅用户                               │
│  - 输出 {企业用户名: [变更路径]} JSON                     │
└─────────────────────────────────────────────────────────┘
```

## 目录结构

```
├── app.yml                    # 蓝鲸PaaS应用描述文件
├── runtime.txt                # Python运行时版本
├── requirements.txt           # Python依赖
├── manage.py                  # Django管理脚本
├── wsgi.py                    # WSGI入口
├── urls.py                    # 根URL配置
├── config/                    # 配置文件
│   ├── default.py            # 基础配置
│   ├── dev.py                # 开发环境配置
│   ├── stag.py               # 测试环境配置
│   └── prod.py               # 生产环境配置
├── home_application/          # 首页应用
│   ├── models.py             # UserProfile模型（企业用户名绑定）
│   ├── middleware.py         # 企业用户名绑定中间件
│   └── views.py              # 首页和用户名绑定视图
├── subscription/              # 订阅管理应用
│   ├── models.py             # GitLabProject、Subscription模型
│   ├── views.py              # Web页面视图
│   ├── api_views.py          # REST API视图
│   ├── gitlab_service.py     # GitLab API封装
│   ├── iam_permissions.py    # 蓝鲸权限中心集成
│   └── authentication.py    # 运行端Token认证
├── templates/                 # HTML模板
├── static/                    # 静态资源
├── runner/                    # 运行端脚本
│   └── gitlab_runner.py      # CI/CD集成脚本
└── bin/
    └── pre-release.sh        # 部署前钩子脚本
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 本地开发（无需蓝鲸PaaS）

```bash
# 启用Mock登录模式
export ENABLE_MOCK_LOGIN=True
export DJANGO_SETTINGS_MODULE=config.dev

# 初始化数据库
python manage.py migrate

# 创建管理员账号
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

访问 http://localhost:8000 即可看到应用界面。

### 3. 蓝鲸PaaS部署

1. 在蓝鲸PaaS控制台创建应用（应用ID: `bk_gitlab_sub`）
2. 将代码推送到蓝鲸代码仓库或通过S-mart上传
3. 配置环境变量（见下方）
4. 部署应用

### 4. 环境变量配置

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `APP_CODE` | 是 | 蓝鲸应用ID |
| `SECRET_KEY` | 是 | 蓝鲸应用密钥 |
| `BK_PAAS_HOST` | 是 | 蓝鲸PaaS地址 |
| `BK_IAM_HOST` | 否 | 权限中心地址 |
| `MYSQL_NAME` | 生产必填 | MySQL数据库名 |
| `MYSQL_USER` | 生产必填 | MySQL用户名 |
| `MYSQL_PASSWORD` | 生产必填 | MySQL密码 |
| `MYSQL_HOST` | 生产必填 | MySQL主机 |
| `RUNNER_API_TOKEN` | 否 | 运行端API令牌 |

## 权限说明

本系统集成蓝鲸权限中心（IAM），包含两类权限：

| 权限名称 | 权限ID | 说明 |
|---------|--------|------|
| 基础功能授权 | `view_project` | 可查看项目列表、创建自己的订阅 |
| 全量数据管理权限 | `manage_project` | 可创建/编辑/删除项目，管理所有用户订阅 |

## 运行端脚本使用

### 在GitLab CI中使用

```yaml
# .gitlab-ci.yml
stages:
  - notify

notify-subscribers:
  stage: notify
  script:
    - |
      CHANGED_FILES=$(git diff --name-only $CI_MERGE_REQUEST_DIFF_BASE_SHA $CI_COMMIT_SHA | python3 -c "
      import sys, json; print(json.dumps(sys.stdin.read().strip().splitlines()))
      ")
      RESULT=$(python3 runner/gitlab_runner.py $MANAGEMENT_PROJECT_ID "$CHANGED_FILES" $CI_MERGE_REQUEST_TARGET_BRANCH_NAME)
      echo "Matched subscribers: $RESULT"
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  variables:
    BK_GITLAB_SUB_API_URL: "https://your-bk-paas.example.com/o/bk_gitlab_sub"
    BK_APP_CODE: "your_app_code"
    BK_APP_SECRET: "your_app_secret"
    MANAGEMENT_PROJECT_ID: "1"
```

### 命令行直接调用

```bash
export BK_GITLAB_SUB_API_URL="https://your-bk-paas.example.com/o/bk_gitlab_sub"
export BK_APP_CODE="bk_gitlab_sub"
export BK_APP_SECRET="your-app-secret"

python3 runner/gitlab_runner.py 1 '["src/main.py", "docs/README.md"]' main
```

输出示例：
```json
{
  "zhangsan": ["src/main.py"],
  "lisi": ["docs/README.md", "src/main.py"]
}
```

## API说明

### Runner API（供运行端脚本调用）

**POST** `/api/runner/changes/`

请求头：
```
X-Bk-App-Code: <app_code>
X-Bk-App-Secret: <app_secret>
```

请求体：
```json
{
  "project_id": 1,
  "changed_files": ["src/main.py", "docs/README.md"],
  "target_branch": "main"
}
```

响应：
```json
{
  "result": true,
  "data": {
    "zhangsan": ["src/main.py"],
    "lisi": ["docs/README.md"]
  }
}
```
