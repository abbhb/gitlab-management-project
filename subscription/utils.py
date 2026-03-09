"""Utility functions for subscription app."""
import logging

from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework.
    Returns standardized error responses.
    """
    response = exception_handler(exc, context)

    if response is not None:
        return Response(
            {
                "result": False,
                "code": response.status_code,
                "message": str(exc),
                "data": response.data,
            },
            status=response.status_code,
        )

    logger.exception("Unhandled exception in API view: %s", exc)
    return Response(
        {
            "result": False,
            "code": 500,
            "message": "服务器内部错误，请稍后重试",
            "data": None,
        },
        status=500,
    )


def api_success(data=None, message="success"):
    """Return a standardized success API response."""
    return Response({"result": True, "code": 200, "message": message, "data": data})


def api_error(message, code=400, data=None):
    """Return a standardized error API response."""
    return Response({"result": False, "code": code, "message": message, "data": data}, status=code)


def match_changed_files_to_subscriptions(changed_files, subscriptions):
    """
    Match a list of changed files to subscriptions and build user->changes mapping.

    Args:
        changed_files: List of file paths that were changed
        subscriptions: QuerySet of Subscription objects

    Returns:
        dict: {enterprise_username: [matched_paths]}
    """
    user_changes = {}

    for subscription in subscriptions:
        matched_paths = []
        for file_path in changed_files:
            if subscription.matches_path(file_path):
                matched_paths.append(file_path)

        if matched_paths:
            try:
                enterprise_username = subscription.user.profile.enterprise_username
            except Exception:
                logger.warning(
                    "User %s has no enterprise username binding, skipping",
                    subscription.user.username,
                )
                continue

            if enterprise_username not in user_changes:
                user_changes[enterprise_username] = []

            # Add unique paths only
            for path in matched_paths:
                if path not in user_changes[enterprise_username]:
                    user_changes[enterprise_username].append(path)

    return user_changes
