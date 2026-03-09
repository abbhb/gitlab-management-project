"""Forms for subscription app."""
from django import forms

from subscription.models import GitLabProject, Subscription


class GitLabProjectForm(forms.ModelForm):
    """Form for creating and editing GitLab projects."""

    class Meta:
        model = GitLabProject
        fields = ["name", "description", "gitlab_url", "gitlab_project_id", "gitlab_token", "default_branch", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "bk-form-input", "placeholder": "项目名称"}),
            "description": forms.Textarea(attrs={"class": "bk-form-textarea", "rows": 3}),
            "gitlab_url": forms.URLInput(attrs={"class": "bk-form-input", "placeholder": "https://gitlab.com"}),
            "gitlab_project_id": forms.NumberInput(attrs={"class": "bk-form-input", "placeholder": "GitLab项目ID"}),
            "gitlab_token": forms.PasswordInput(
                attrs={"class": "bk-form-input", "placeholder": "Personal Access Token"},
                render_value=False,
            ),
            "default_branch": forms.TextInput(attrs={"class": "bk-form-input", "placeholder": "main"}),
        }
        labels = {
            "name": "项目名称",
            "description": "项目描述",
            "gitlab_url": "GitLab地址",
            "gitlab_project_id": "GitLab项目ID",
            "gitlab_token": "访问令牌",
            "default_branch": "默认分支",
            "is_active": "启用",
        }
        help_texts = {
            "gitlab_url": "GitLab实例URL，例如：https://gitlab.com 或内网地址",
            "gitlab_project_id": "在GitLab项目设置中可找到项目ID",
            "gitlab_token": "需要有read_repository权限的Token",
        }

    def clean(self):
        cleaned_data = super().clean()
        gitlab_url = cleaned_data.get("gitlab_url")
        gitlab_project_id = cleaned_data.get("gitlab_project_id")
        gitlab_token = cleaned_data.get("gitlab_token")

        if gitlab_url and gitlab_project_id and gitlab_token:
            from subscription.gitlab_service import GitLabService

            service = GitLabService(gitlab_url, gitlab_token)
            if not service.validate_token(gitlab_project_id):
                raise forms.ValidationError("无法访问指定的GitLab项目，请检查Token和项目ID是否正确")
        return cleaned_data


class SubscriptionForm(forms.ModelForm):
    """Form for creating subscriptions."""

    def __init__(self, *args, project=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.project = project
        if project:
            self.fields["branch"].initial = project.default_branch

    class Meta:
        model = Subscription
        fields = ["path", "path_type", "branch"]
        widgets = {
            "path": forms.TextInput(
                attrs={"class": "bk-form-input", "placeholder": "src/ 或 src/main.py"}
            ),
            "path_type": forms.Select(attrs={"class": "bk-form-select"}),
            "branch": forms.TextInput(attrs={"class": "bk-form-input"}),
        }
        labels = {
            "path": "订阅路径",
            "path_type": "路径类型",
            "branch": "目标分支",
        }
        help_texts = {
            "path": "目录路径以/结尾（如 src/），文件路径不加/（如 src/main.py）",
            "branch": "订阅的目标分支，当MR合入该分支时触发通知",
        }

    def clean_path(self):
        path = self.cleaned_data["path"].strip()
        if not path:
            raise forms.ValidationError("路径不能为空")
        # Normalize path: remove leading slash
        if path.startswith("/"):
            path = path[1:]
        return path

    def clean(self):
        cleaned_data = super().clean()
        if self.project and self.instance.pk is None:
            path = cleaned_data.get("path")
            branch = cleaned_data.get("branch")
            from django.contrib.auth import get_user_model

            User = get_user_model()
            if path and branch:
                # Check for duplicate (will be handled by unique_together in DB)
                pass
        return cleaned_data
