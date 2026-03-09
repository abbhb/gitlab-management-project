"""Middleware for core."""
import logging

from django.conf import settings
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

# Paths that should not require enterprise username binding
EXEMPT_PATHS = [
    "/account/bind-username/",
    "/account/bind-username",
    "/static/",
    "/admin/",
    "/favicon.ico",
    "/api/",  # API endpoints use token auth, no binding required
]


class EnterpriseUsernameBindingMiddleware:
    """
    Middleware that enforces enterprise username binding on first login.

    If a logged-in user does not have a UserProfile (enterprise username),
    they are redirected to the binding page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not self._is_exempt(request.path):
            from core.models import UserProfile

            try:
                request.user.profile
            except UserProfile.DoesNotExist:
                return redirect("core:bind_username")

        response = self.get_response(request)
        return response

    @staticmethod
    def _is_exempt(path):
        """Check if the path is exempt from username binding check."""
        for exempt_path in EXEMPT_PATHS:
            if path.startswith(exempt_path):
                return True
        return False


class MockLoginMiddleware:
    """
    Development-only middleware to simulate BlueKing login without PaaS.
    Creates a test user for local development.

    Only active when ENABLE_MOCK_LOGIN=True in settings.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            from django.contrib.auth import get_user_model, login

            User = get_user_model()
            user, _ = User.objects.get_or_create(
                username="dev_user",
                defaults={
                    "is_staff": True,
                    "is_superuser": True,
                },
            )
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            logger.debug("MockLoginMiddleware: logged in as dev_user")

        response = self.get_response(request)
        return response
