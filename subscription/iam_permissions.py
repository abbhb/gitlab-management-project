"""IAM permission integration for subscription app."""
import logging

from django.conf import settings

logger = logging.getLogger(__name__)

# IAM Action IDs
ACTION_VIEW_PROJECT = "view_project"
ACTION_MANAGE_PROJECT = "manage_project"
ACTION_CREATE_SUBSCRIPTION = "create_subscription"
ACTION_MANAGE_ALL = "manage_all"

# IAM Resource Types
RESOURCE_PROJECT = "gitlab_project"


def get_iam_client():
    """Get IAM client instance."""
    if getattr(settings, "BK_IAM_SKIP", False):
        return None
    try:
        from iam import IAM

        return IAM(
            app_code=settings.BK_APP_CODE,
            app_secret=settings.BK_APP_SECRET,
            bk_iam_host=settings.BK_IAM_HOST,
            bk_paas_host=settings.BK_PAAS_HOST,
        )
    except ImportError:
        logger.warning("bk-iam package not installed, IAM checks will be skipped")
        return None


def is_allowed(request, action, resource_type=None, resource_id=None):
    """
    Check if the current user has permission to perform an action.

    Args:
        request: Django request object
        action: IAM action ID
        resource_type: IAM resource type (optional)
        resource_id: Resource instance ID (optional)

    Returns:
        bool: True if allowed, False otherwise
    """
    if getattr(settings, "BK_IAM_SKIP", False):
        # In development/skip mode, allow superusers and staff to manage
        if action in [ACTION_MANAGE_PROJECT, ACTION_MANAGE_ALL]:
            return request.user.is_staff or request.user.is_superuser
        return True

    iam_client = get_iam_client()
    if iam_client is None:
        # Fall back to Django permission model
        if action in [ACTION_MANAGE_PROJECT, ACTION_MANAGE_ALL]:
            return request.user.is_staff or request.user.is_superuser
        return request.user.is_authenticated

    try:
        from iam import Action, Request, Resource, Subject

        subject = Subject("user", request.user.username)
        iam_action = Action(action)

        resources = []
        if resource_type and resource_id:
            resources = [Resource(resource_type, str(resource_id), {})]

        iam_request = Request(
            system=settings.BK_IAM_SYSTEM_ID,
            subject=subject,
            action=iam_action,
            resources=resources,
            environment={},
        )
        return iam_client.is_allowed(iam_request)
    except Exception as e:
        logger.error("IAM permission check failed: %s", e)
        # Fail open for basic actions, fail closed for admin actions
        if action in [ACTION_MANAGE_PROJECT, ACTION_MANAGE_ALL]:
            return False
        return True


def get_apply_url(request, action, resource_type=None, resource_id=None):
    """
    Get the URL for users to apply for permissions.

    Args:
        request: Django request object
        action: IAM action ID
        resource_type: IAM resource type (optional)
        resource_id: Resource instance ID (optional)

    Returns:
        str: URL to the IAM permission application page
    """
    iam_client = get_iam_client()
    if iam_client is None:
        return ""

    try:
        from iam import Action, Resource, Subject
        from iam.apply.models import ActionWithoutResources, ActionWithResources, RelatedResourceType

        subject = Subject("user", request.user.username)

        if resource_type and resource_id:
            related_resource_types = [
                RelatedResourceType(
                    system_id=settings.BK_IAM_SYSTEM_ID,
                    type=resource_type,
                    instances=[[{"type": resource_type, "id": str(resource_id)}]],
                )
            ]
            actions = [ActionWithResources(id=action, related_resource_types=related_resource_types)]
        else:
            actions = [ActionWithoutResources(id=action)]

        application = {"actions": actions}
        url = iam_client.get_apply_url(application, subject)
        return url
    except Exception as e:
        logger.error("Failed to get IAM apply URL: %s", e)
        return ""
