"""Custom authentication classes for subscription app."""
import logging

from django.conf import settings
from rest_framework import authentication, exceptions
from rest_framework.authentication import SessionAuthentication

logger = logging.getLogger(__name__)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """Session authentication that does not enforce CSRF checks."""

    def enforce_csrf(self, request):
        return


class AppTokenAuthentication(authentication.BaseAuthentication):
    """
    Authentication for CI/CD runner scripts.

    Expects the following headers:
      X-Bk-App-Code: <app_code>
      X-Bk-App-Secret: <app_secret>

    This allows the runner script to authenticate against the management API
    without needing a user session.
    """

    def authenticate(self, request):
        app_code = request.META.get("HTTP_X_BK_APP_CODE", "")
        app_secret = request.META.get("HTTP_X_BK_APP_SECRET", "")

        if not app_code or not app_secret:
            return None

        # Validate app credentials
        if app_code == settings.BK_APP_CODE and app_secret == settings.BK_APP_SECRET:
            # Create a system user for the runner
            from django.contrib.auth import get_user_model

            User = get_user_model()
            try:
                user = User.objects.get(username="__runner__")
            except User.DoesNotExist:
                user = User.objects.create(
                    username="__runner__",
                    is_active=True,
                    is_staff=False,
                    is_superuser=False,
                )
            return (user, "app_token")

        raise exceptions.AuthenticationFailed("Invalid app credentials")

    def authenticate_header(self, request):
        return "AppToken"
