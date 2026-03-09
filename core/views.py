"""Views for core."""
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.frontend import build_frontend_context
from core.forms import BindUsernameForm
from core.models import UserProfile

logger = logging.getLogger(__name__)


def index(request):
    """Home page - rendered by the Vue frontend shell."""
    if not request.user.is_authenticated:
        from django.conf import settings

        return redirect(settings.LOGIN_URL)

    try:
        request.user.profile
    except UserProfile.DoesNotExist:
        return redirect("core:bind_username")

    return render(request, "frontend/app.html", build_frontend_context(request, "dashboard"))


@login_required
def bind_username(request):
    """
    Page for binding enterprise username on first login.

    Redirects to home after successful binding.
    """
    # If already bound, redirect to home
    try:
        request.user.profile
        return redirect("core:index")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = BindUsernameForm(request.POST)
        if form.is_valid():
            enterprise_username = form.cleaned_data["enterprise_username"]
            UserProfile.objects.create(
                user=request.user,
                enterprise_username=enterprise_username,
            )
            messages.success(request, f"企业用户名 {enterprise_username} 绑定成功！")
            logger.info(
                "User %s bound enterprise username: %s",
                request.user.username,
                enterprise_username,
            )
            return redirect("core:index")
    else:
        form = BindUsernameForm()

    return render(request, "subscription/bind_username.html", {"form": form})
