"""Forms for home_application."""
from django import forms


class BindUsernameForm(forms.Form):
    """Form for binding enterprise username."""

    enterprise_username = forms.CharField(
        max_length=100,
        label="企业用户名",
        help_text="请输入您的企业内部用户名（用于接收变更通知）",
        widget=forms.TextInput(
            attrs={
                "class": "bk-form-input",
                "placeholder": "请输入企业用户名",
                "autofocus": True,
            }
        ),
    )

    def clean_enterprise_username(self):
        from home_application.models import UserProfile

        username = self.cleaned_data["enterprise_username"].strip()
        if not username:
            raise forms.ValidationError("企业用户名不能为空")
        if UserProfile.objects.filter(enterprise_username=username).exists():
            raise forms.ValidationError("该企业用户名已被其他账户绑定，请联系管理员")
        return username
