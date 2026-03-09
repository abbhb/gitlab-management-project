"""Models for home_application."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    """
    User profile model that stores enterprise (corporate) username binding.

    Every user must bind an enterprise username on first login to identify
    themselves in the subscription notification system.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="登录用户",
    )
    enterprise_username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="企业用户名",
        help_text="用于在通知中标识用户的企业内部用户名",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "用户档案"
        verbose_name_plural = "用户档案"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} -> {self.enterprise_username}"
