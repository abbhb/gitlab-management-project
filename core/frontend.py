"""Helpers for rendering the Vue frontend shell."""
# pyright: reportMissingTypeStubs=false, reportMissingParameterType=false, reportUnknownParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false, reportUnknownLambdaType=false, reportMissingTypeArgument=false
import os

from django.conf import settings  # type: ignore[import-not-found]
from django.middleware.csrf import get_token  # type: ignore[import-not-found]


def build_frontend_context(request, page, **page_props):
    """Build template context consumed by the frontend app."""
    enterprise_username = ""
    try:
        enterprise_username = request.user.profile.enterprise_username
    except Exception:
        enterprise_username = ""

    return {
        "frontend_config": {
            "page": page,
            "pageProps": page_props,
            "csrfToken": get_token(request),
            "user": {
                "username": getattr(request.user, "username", ""),
                "enterprise_username": enterprise_username,
            },
            "urls": {
                "home": "/",
                "projectList": "/subscription/projects/",
                "subscriptionList": "/subscription/my-subscriptions/",
                "console": getattr(settings, "BK_PAAS_HOST", "") + "/console/",
                "logout": "{host}/login/logout/?app_id={app_code}".format(
                    host=getattr(settings, "BK_PAAS_HOST", ""),
                    app_code=getattr(settings, "BK_APP_CODE", ""),
                ),
            },
        },
        "frontend_template_ready": os.path.exists(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates", "frontend", "app.html")
        ),
    }