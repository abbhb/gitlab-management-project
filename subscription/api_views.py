"""API views for subscription app."""
import logging

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from subscription.authentication import AppTokenAuthentication, CsrfExemptSessionAuthentication
from subscription.gitlab_service import GitLabService
from subscription.iam_permissions import ACTION_MANAGE_PROJECT, ACTION_VIEW_PROJECT, is_allowed
from subscription.models import GitLabProject, Subscription
from subscription.serializers import (
    GitLabProjectCreateSerializer,
    GitLabProjectSerializer,
    RunnerChangesRequestSerializer,
    SubscriptionSerializer,
)
from subscription.utils import api_error, api_success, match_changed_files_to_subscriptions

logger = logging.getLogger(__name__)


class ProjectListAPIView(APIView):
    """
    API endpoint for listing and creating GitLab projects.

    GET  /api/projects/      - List all active projects
    POST /api/projects/      - Create a new project (admin only)
    """

    def get(self, request):
        if not is_allowed(request, ACTION_VIEW_PROJECT):
            return api_error("无权限查看项目列表", code=403)

        projects = GitLabProject.objects.filter(is_active=True).order_by("-created_at")
        serializer = GitLabProjectSerializer(projects, many=True)
        return api_success(data=serializer.data)

    def post(self, request):
        if not is_allowed(request, ACTION_MANAGE_PROJECT):
            return api_error("无权限创建项目，需要管理员权限", code=403)

        serializer = GitLabProjectCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            project = serializer.save()
            return api_success(
                data=GitLabProjectSerializer(project).data,
                message="项目创建成功",
            )
        return api_error("请求参数有误", data=serializer.errors)


class ProjectDetailAPIView(APIView):
    """
    API endpoint for retrieving, updating, and deleting a specific project.

    GET    /api/projects/{id}/  - Get project details
    PUT    /api/projects/{id}/  - Update project (admin only)
    DELETE /api/projects/{id}/  - Delete project (admin only)
    """

    def get_project(self, project_id):
        try:
            return GitLabProject.objects.get(id=project_id)
        except GitLabProject.DoesNotExist:
            return None

    def get(self, request, project_id):
        if not is_allowed(request, ACTION_VIEW_PROJECT):
            return api_error("无权限查看项目", code=403)

        project = self.get_project(project_id)
        if not project:
            return api_error("项目不存在", code=404)

        serializer = GitLabProjectSerializer(project)
        return api_success(data=serializer.data)

    def put(self, request, project_id):
        if not is_allowed(request, ACTION_MANAGE_PROJECT):
            return api_error("无权限修改项目", code=403)

        project = self.get_project(project_id)
        if not project:
            return api_error("项目不存在", code=404)

        serializer = GitLabProjectCreateSerializer(project, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            project = serializer.save()
            return api_success(data=GitLabProjectSerializer(project).data, message="项目更新成功")
        return api_error("请求参数有误", data=serializer.errors)

    def delete(self, request, project_id):
        if not is_allowed(request, ACTION_MANAGE_PROJECT):
            return api_error("无权限删除项目", code=403)

        project = self.get_project(project_id)
        if not project:
            return api_error("项目不存在", code=404)

        project.is_active = False
        project.save()
        return api_success(message="项目已停用")


class GitLabBranchesAPIView(APIView):
    """
    API endpoint to fetch branches for a GitLab project.

    GET /api/projects/{id}/branches/
    """

    def get(self, request, project_id):
        if not is_allowed(request, ACTION_VIEW_PROJECT):
            return api_error("无权限", code=403)

        try:
            project = GitLabProject.objects.get(id=project_id, is_active=True)
        except GitLabProject.DoesNotExist:
            return api_error("项目不存在", code=404)

        try:
            service = GitLabService(project.gitlab_url, project.gitlab_token)
            branches = service.get_branches(project.gitlab_project_id)
            return api_success(data=branches)
        except Exception as e:
            logger.error("Failed to fetch branches for project %s: %s", project_id, e)
            return api_error(f"无法获取GitLab分支信息: {str(e)}", code=502)


class GitLabFileTreeAPIView(APIView):
    """
    API endpoint to fetch file tree for a GitLab project.

    GET /api/projects/{id}/tree/?path=src&branch=main&recursive=false
    """

    def get(self, request, project_id):
        if not is_allowed(request, ACTION_VIEW_PROJECT):
            return api_error("无权限", code=403)

        try:
            project = GitLabProject.objects.get(id=project_id, is_active=True)
        except GitLabProject.DoesNotExist:
            return api_error("项目不存在", code=404)

        path = request.query_params.get("path", "")
        branch = request.query_params.get("branch", project.default_branch)
        recursive = request.query_params.get("recursive", "false").lower() == "true"

        try:
            service = GitLabService(project.gitlab_url, project.gitlab_token)
            tree = service.get_file_tree(project.gitlab_project_id, path=path, branch=branch, recursive=recursive)
            return api_success(data=tree)
        except Exception as e:
            logger.error("Failed to fetch file tree for project %s: %s", project_id, e)
            return api_error(f"无法获取GitLab文件树: {str(e)}", code=502)


class SubscriptionListAPIView(APIView):
    """
    API endpoint for listing and creating subscriptions.

    GET  /api/subscriptions/  - List current user's subscriptions
    POST /api/subscriptions/  - Create a new subscription
    """

    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user).select_related("project")
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return api_success(data=serializer.data)

    def post(self, request):
        if not is_allowed(request, ACTION_VIEW_PROJECT):
            return api_error("无权限订阅", code=403)

        serializer = SubscriptionSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            subscription = serializer.save()
            return api_success(
                data=SubscriptionSerializer(subscription).data,
                message="订阅创建成功",
            )
        return api_error("请求参数有误", data=serializer.errors)


class SubscriptionDetailAPIView(APIView):
    """
    API endpoint for retrieving and deleting a specific subscription.

    GET    /api/subscriptions/{id}/
    DELETE /api/subscriptions/{id}/
    """

    def get_subscription(self, subscription_id, user):
        try:
            return Subscription.objects.get(id=subscription_id, user=user)
        except Subscription.DoesNotExist:
            return None

    def get(self, request, subscription_id):
        subscription = self.get_subscription(subscription_id, request.user)
        if not subscription:
            return api_error("订阅不存在", code=404)
        serializer = SubscriptionSerializer(subscription)
        return api_success(data=serializer.data)

    def delete(self, request, subscription_id):
        subscription = self.get_subscription(subscription_id, request.user)
        if not subscription:
            # Check if admin is deleting someone else's subscription
            if is_allowed(request, ACTION_MANAGE_PROJECT):
                try:
                    subscription = Subscription.objects.get(id=subscription_id)
                except Subscription.DoesNotExist:
                    return api_error("订阅不存在", code=404)
            else:
                return api_error("订阅不存在或无权限删除", code=404)

        subscription.delete()
        return api_success(message="订阅已删除")


@api_view(["POST"])
@authentication_classes([CsrfExemptSessionAuthentication, AppTokenAuthentication])
@permission_classes([IsAuthenticated])
def runner_changes_api(request):
    """
    Runner API endpoint for CI/CD pipeline integration.

    Given a project ID and list of changed files, returns a mapping of
    enterprise usernames to their relevant changed paths based on subscriptions.

    This endpoint is authenticated using App Token (X-Bk-App-Code + X-Bk-App-Secret).
    It is CSRF-exempt since it uses token-based authentication.

    Request body:
        {
            "project_id": 1,
            "changed_files": ["src/main.py", "docs/README.md"],
            "target_branch": "main"  // optional
        }

    Response:
        {
            "result": true,
            "data": {
                "user1_enterprise": ["src/main.py"],
                "user2_enterprise": ["docs/README.md"]
            }
        }
    """
    serializer = RunnerChangesRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return api_error("请求参数有误", data=serializer.errors)

    project_id = serializer.validated_data["project_id"]
    changed_files = serializer.validated_data["changed_files"]
    target_branch = serializer.validated_data.get("target_branch", "")

    try:
        project = GitLabProject.objects.get(id=project_id, is_active=True)
    except GitLabProject.DoesNotExist:
        return api_error(f"项目ID {project_id} 不存在或已停用", code=404)

    # Get subscriptions for this project, optionally filtered by branch
    subscriptions = Subscription.objects.filter(project=project).select_related("user", "user__profile")
    if target_branch:
        subscriptions = subscriptions.filter(branch=target_branch)

    user_changes = match_changed_files_to_subscriptions(changed_files, subscriptions)

    logger.info(
        "Runner API: project=%s, changed_files=%d, matched_users=%d",
        project_id,
        len(changed_files),
        len(user_changes),
    )

    return api_success(data=user_changes)
