"""Admin configuration for home_application."""
from django.contrib import admin

from home_application.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "enterprise_username", "created_at"]
    search_fields = ["user__username", "enterprise_username"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
