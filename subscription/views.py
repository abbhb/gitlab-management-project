"""Views for subscription app (web pages)."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from core.frontend import build_frontend_context
from subscription.iam_permissions import ACTION_MANAGE_PROJECT, ACTION_VIEW_PROJECT, is_allowed
from subscription.models import GitLabProject, Subscription


@login_required
def project_list(request):
    """Render the project list frontend page."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限查看项目列表，请申请相应权限")
        return render(request, "subscription/no_permission.html", status=403)

    return render(request, "frontend/app.html", build_frontend_context(request, "project-list"))


@login_required
def project_create(request):
    """Render the project create frontend page."""
    if not is_allowed(request, ACTION_MANAGE_PROJECT):
        messages.error(request, "您没有权限创建项目，请申请管理权限")
        return render(request, "subscription/no_permission.html", status=403)

    return render(request, "frontend/app.html", build_frontend_context(request, "project-form", mode="create"))


@login_required
def project_edit(request, project_id):
    """Render the project edit frontend page."""
    if not is_allowed(request, ACTION_MANAGE_PROJECT):
        messages.error(request, "您没有权限编辑项目")
        return render(request, "subscription/no_permission.html", status=403)

    get_object_or_404(GitLabProject, id=project_id)
    return render(
        request,
        "frontend/app.html",
        build_frontend_context(request, "project-form", mode="edit", projectId=project_id),
    )


@login_required
def project_detail(request, project_id):
    """Render the project detail frontend page."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限查看项目")
        return render(request, "subscription/no_permission.html", status=403)

    get_object_or_404(GitLabProject, id=project_id, is_active=True)
    return render(
        request,
        "frontend/app.html",
        build_frontend_context(request, "project-detail", projectId=project_id),
    )


@login_required
def subscription_list(request):
    """Render the current user's subscription list frontend page."""
    return render(request, "frontend/app.html", build_frontend_context(request, "subscription-list"))


@login_required
def subscription_create(request, project_id):
    """Render the subscription create frontend page."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限订阅，请申请相应权限")
        return render(request, "subscription/no_permission.html", status=403)

    get_object_or_404(GitLabProject, id=project_id, is_active=True)
    return render(
        request,
        "frontend/app.html",
        build_frontend_context(request, "subscription-form", projectId=project_id),
    )


@login_required
def subscription_delete(request, subscription_id):
    """Delete a subscription (owner or admin only)."""
    subscription = get_object_or_404(Subscription, id=subscription_id)

    # Only subscription owner or admin can delete
    if subscription.user != request.user and not is_allowed(request, ACTION_MANAGE_PROJECT):
        messages.error(request, "您没有权限删除此订阅")
        return redirect("subscription:subscription_list")

    if request.method == "POST":
        project_id = subscription.project.id
        subscription.delete()
        messages.success(request, "订阅已删除")
        return redirect("subscription:project_detail", project_id=project_id)

    return render(request, "subscription/subscription_confirm_delete.html", {"subscription": subscription})
