"""Views for subscription app (web pages)."""
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from subscription.forms import GitLabProjectForm, SubscriptionForm
from subscription.gitlab_service import GitLabService
from subscription.iam_permissions import ACTION_MANAGE_PROJECT, ACTION_VIEW_PROJECT, is_allowed
from subscription.models import GitLabProject, Subscription

logger = logging.getLogger(__name__)


@login_required
def project_list(request):
    """List all active GitLab projects."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限查看项目列表，请申请相应权限")
        return render(request, "subscription/no_permission.html", status=403)

    projects = GitLabProject.objects.filter(is_active=True).order_by("-created_at")

    # Annotate each project with user's subscription count
    for project in projects:
        project.user_sub_count = project.subscriptions.filter(user=request.user).count()

    context = {
        "projects": projects,
        "can_manage": is_allowed(request, ACTION_MANAGE_PROJECT),
    }
    return render(request, "subscription/project_list.html", context)


@login_required
def project_create(request):
    """Create a new GitLab project (admin only)."""
    if not is_allowed(request, ACTION_MANAGE_PROJECT):
        messages.error(request, "您没有权限创建项目，请申请管理权限")
        return render(request, "subscription/no_permission.html", status=403)

    if request.method == "POST":
        form = GitLabProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, f"项目 {project.name} 创建成功！")
            return redirect("subscription:project_list")
    else:
        form = GitLabProjectForm()

    return render(request, "subscription/project_form.html", {"form": form, "action": "创建"})


@login_required
def project_edit(request, project_id):
    """Edit an existing GitLab project (admin only)."""
    if not is_allowed(request, ACTION_MANAGE_PROJECT):
        messages.error(request, "您没有权限编辑项目")
        return render(request, "subscription/no_permission.html", status=403)

    project = get_object_or_404(GitLabProject, id=project_id)

    if request.method == "POST":
        form = GitLabProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"项目 {project.name} 更新成功！")
            return redirect("subscription:project_list")
    else:
        form = GitLabProjectForm(instance=project)

    return render(
        request,
        "subscription/project_form.html",
        {"form": form, "project": project, "action": "编辑"},
    )


@login_required
def project_detail(request, project_id):
    """Show project details and user's subscriptions for this project."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限查看项目")
        return render(request, "subscription/no_permission.html", status=403)

    project = get_object_or_404(GitLabProject, id=project_id, is_active=True)
    user_subscriptions = Subscription.objects.filter(user=request.user, project=project)

    context = {
        "project": project,
        "subscriptions": user_subscriptions,
        "can_manage": is_allowed(request, ACTION_MANAGE_PROJECT),
    }
    return render(request, "subscription/project_detail.html", context)


@login_required
def subscription_list(request):
    """List current user's subscriptions."""
    subscriptions = Subscription.objects.filter(user=request.user).select_related("project").order_by("-created_at")
    context = {"subscriptions": subscriptions}
    return render(request, "subscription/subscription_list.html", context)


@login_required
def subscription_create(request, project_id):
    """Create a new subscription for the current user."""
    if not is_allowed(request, ACTION_VIEW_PROJECT):
        messages.error(request, "您没有权限订阅，请申请相应权限")
        return render(request, "subscription/no_permission.html", status=403)

    project = get_object_or_404(GitLabProject, id=project_id, is_active=True)

    if request.method == "POST":
        form = SubscriptionForm(request.POST, project=project)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.project = project
            subscription.save()
            messages.success(request, f"成功订阅 {project.name} 的路径: {subscription.path}")
            return redirect("subscription:project_detail", project_id=project_id)
    else:
        form = SubscriptionForm(project=project)

    # Get file tree for the UI
    file_tree = []
    branches = []
    try:
        service = GitLabService(project.gitlab_url, project.gitlab_token)
        branches = service.get_branches(project.gitlab_project_id)
        selected_branch = request.GET.get("branch", project.default_branch)
        file_tree = service.get_file_tree(project.gitlab_project_id, branch=selected_branch)
    except Exception as e:
        logger.warning("Failed to load GitLab tree for project %s: %s", project_id, e)
        messages.warning(request, "无法加载GitLab文件树，请手动输入路径")

    context = {
        "form": form,
        "project": project,
        "file_tree": file_tree,
        "branches": branches,
    }
    return render(request, "subscription/subscription_form.html", context)


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
