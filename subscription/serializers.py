"""Serializers for subscription app."""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from subscription.models import GitLabProject, Subscription

User = get_user_model()


class GitLabProjectSerializer(serializers.ModelSerializer):
    """Serializer for GitLabProject model."""

    created_by_username = serializers.CharField(source="created_by.username", read_only=True)
    subscription_count = serializers.SerializerMethodField()
    user_sub_count = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = GitLabProject
        fields = [
            "id",
            "name",
            "description",
            "gitlab_url",
            "gitlab_project_id",
            "default_branch",
            "created_by",
            "created_by_username",
            "created_at",
            "updated_at",
            "is_active",
            "subscription_count",
            "user_sub_count",
        ]
        read_only_fields = ["id", "created_by", "created_at", "updated_at"]
        extra_kwargs = {
            "gitlab_token": {"write_only": True},
        }

    def get_subscription_count(self, obj):
        annotated_value = getattr(obj, "subscription_count", None)
        if annotated_value is not None:
            return annotated_value
        return obj.subscriptions.count()


class GitLabProjectCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating GitLabProject (includes token)."""

    class Meta:
        model = GitLabProject
        fields = [
            "id",
            "name",
            "description",
            "gitlab_url",
            "gitlab_project_id",
            "gitlab_token",
            "default_branch",
            "is_active",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        """Validate GitLab token by trying to access the project."""
        from subscription.gitlab_service import GitLabService

        gitlab_url = attrs.get("gitlab_url")
        gitlab_project_id = attrs.get("gitlab_project_id")
        gitlab_token = attrs.get("gitlab_token")

        if gitlab_url and gitlab_project_id and gitlab_token:
            service = GitLabService(gitlab_url, gitlab_token)
            if not service.validate_token(gitlab_project_id):
                raise serializers.ValidationError(
                    {"gitlab_token": "无法访问指定的GitLab项目，请检查Token和项目ID是否正确"}
                )
            # Fetch default branch from GitLab if not set
            if not attrs.get("default_branch"):
                try:
                    info = service.get_project_info(gitlab_project_id)
                    attrs["default_branch"] = info.get("default_branch", "main")
                except Exception:
                    pass
        return attrs

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)


class SubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for Subscription model."""

    project_name = serializers.CharField(source="project.name", read_only=True)
    user_username = serializers.CharField(source="user.username", read_only=True)
    enterprise_username = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = [
            "id",
            "user",
            "user_username",
            "enterprise_username",
            "project",
            "project_name",
            "path",
            "path_type",
            "branch",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def get_enterprise_username(self, obj):
        try:
            return obj.user.profile.enterprise_username
        except Exception:
            return ""

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class RunnerChangesRequestSerializer(serializers.Serializer):
    """Serializer for the runner API request payload."""

    project_id = serializers.IntegerField(help_text="管理端GitLab项目ID")
    changed_files = serializers.ListField(
        child=serializers.CharField(max_length=500),
        min_length=1,
        help_text="变更文件路径列表",
    )
    target_branch = serializers.CharField(
        max_length=100,
        required=False,
        default="",
        help_text="目标分支（MR目标分支），不提供则匹配所有分支",
    )


class RunnerChangesResponseSerializer(serializers.Serializer):
    """Serializer for the runner API response."""

    enterprise_username = serializers.CharField()
    changed_paths = serializers.ListField(child=serializers.CharField())
