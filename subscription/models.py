"""Models for subscription app."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GitLabProject(models.Model):
    """
    Represents a GitLab project registered in the subscription system.
    Only administrators can create GitLab projects.
    """

    name = models.CharField(max_length=200, verbose_name="项目名称")
    description = models.TextField(blank=True, default="", verbose_name="项目描述")
    gitlab_url = models.URLField(verbose_name="GitLab地址", help_text="GitLab实例URL，例如：https://gitlab.com")
    gitlab_project_id = models.IntegerField(verbose_name="GitLab项目ID")
    gitlab_token = models.CharField(
        max_length=500,
        verbose_name="GitLab访问令牌",
        help_text="用于拉取GitLab项目信息的Personal Access Token或Project Access Token",
    )
    default_branch = models.CharField(max_length=100, default="main", verbose_name="默认分支")
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_projects",
        verbose_name="创建人",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_active = models.BooleanField(default=True, verbose_name="是否启用")

    class Meta:
        verbose_name = "GitLab项目"
        verbose_name_plural = "GitLab项目"
        ordering = ["-created_at"]
        unique_together = [["gitlab_url", "gitlab_project_id"]]

    def __str__(self):
        return f"{self.name} ({self.gitlab_url}/projects/{self.gitlab_project_id})"


class Subscription(models.Model):
    """
    Represents a user's subscription to a specific path (file or directory)
    within a GitLab project on a specific branch.

    When an MR is created or updated, if the MR changes files matching
    any subscription path, the subscribed user will be notified.
    """

    PATH_TYPE_FILE = "file"
    PATH_TYPE_DIRECTORY = "directory"
    PATH_TYPES = [
        (PATH_TYPE_FILE, "文件"),
        (PATH_TYPE_DIRECTORY, "目录"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="订阅用户",
    )
    project = models.ForeignKey(
        GitLabProject,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="GitLab项目",
    )
    path = models.CharField(
        max_length=500,
        verbose_name="订阅路径",
        help_text="订阅的文件路径或目录路径，目录路径以/结尾",
    )
    path_type = models.CharField(
        max_length=20,
        choices=PATH_TYPES,
        default=PATH_TYPE_DIRECTORY,
        verbose_name="路径类型",
    )
    branch = models.CharField(max_length=100, default="main", verbose_name="目标分支")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "订阅"
        verbose_name_plural = "订阅"
        ordering = ["-created_at"]
        unique_together = [["user", "project", "path", "branch"]]

    def __str__(self):
        return f"{self.user.username} 订阅 {self.project.name}:{self.path}@{self.branch}"

    def matches_path(self, changed_file_path):
        """
        Check if the given changed file path matches this subscription path.

        For directory subscriptions, checks if the changed file is under the directory.
        For file subscriptions, checks for exact match.
        """
        if self.path_type == self.PATH_TYPE_FILE:
            return changed_file_path == self.path
        else:
            # Directory: normalize to ensure trailing slash for proper prefix matching
            dir_path = self.path if self.path.endswith("/") else self.path + "/"
            return changed_file_path.startswith(dir_path) or changed_file_path == self.path.rstrip("/")
