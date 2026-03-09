"""Initial migration for subscription app."""
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GitLabProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="项目名称")),
                ("description", models.TextField(blank=True, default="", verbose_name="项目描述")),
                ("gitlab_url", models.URLField(verbose_name="GitLab地址")),
                ("gitlab_project_id", models.IntegerField(verbose_name="GitLab项目ID")),
                ("gitlab_token", models.CharField(max_length=500, verbose_name="GitLab访问令牌")),
                ("default_branch", models.CharField(default="main", max_length=100, verbose_name="默认分支")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                ("is_active", models.BooleanField(default=True, verbose_name="是否启用")),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="created_projects",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="创建人",
                    ),
                ),
            ],
            options={
                "verbose_name": "GitLab项目",
                "verbose_name_plural": "GitLab项目",
                "ordering": ["-created_at"],
                "unique_together": {("gitlab_url", "gitlab_project_id")},
            },
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "path",
                    models.CharField(max_length=500, verbose_name="订阅路径"),
                ),
                (
                    "path_type",
                    models.CharField(
                        choices=[("file", "文件"), ("directory", "目录")],
                        default="directory",
                        max_length=20,
                        verbose_name="路径类型",
                    ),
                ),
                ("branch", models.CharField(default="main", max_length=100, verbose_name="目标分支")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to="subscription.gitlabproject",
                        verbose_name="GitLab项目",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="订阅用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "订阅",
                "verbose_name_plural": "订阅",
                "ordering": ["-created_at"],
                "unique_together": {("user", "project", "path", "branch")},
            },
        ),
    ]
