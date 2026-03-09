"""Admin configuration for subscription app."""
from django.contrib import admin

from subscription.models import GitLabProject, Subscription


@admin.register(GitLabProject)
class GitLabProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "gitlab_url", "gitlab_project_id", "default_branch", "is_active", "created_by", "created_at"]
    list_filter = ["is_active", "created_at"]
    search_fields = ["name", "gitlab_url", "gitlab_project_id"]
    readonly_fields = ["created_at", "updated_at", "created_by"]
    ordering = ["-created_at"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "project", "path", "path_type", "branch", "created_at"]
    list_filter = ["path_type", "branch", "created_at"]
    search_fields = ["user__username", "project__name", "path"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
