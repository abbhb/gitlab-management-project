"""Context processors for home_application."""
from django.conf import settings


def bk_context(request):
    """Add BlueKing platform context variables to all templates."""
    return {
        "BK_PAAS_HOST": getattr(settings, "BK_PAAS_HOST", ""),
        "BK_APP_CODE": getattr(settings, "BK_APP_CODE", ""),
        "SITE_HEADER": "GitLab订阅管理",
        "SITE_TITLE": "GitLab订阅管理",
    }
