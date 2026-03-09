"""URL configuration for subscription app (REST API endpoints)."""
from django.urls import path

from subscription import api_views

urlpatterns = [
    # Project management API
    path("projects/", api_views.ProjectListAPIView.as_view(), name="api_project_list"),
    path("projects/<int:project_id>/", api_views.ProjectDetailAPIView.as_view(), name="api_project_detail"),
    path("projects/<int:project_id>/branches/", api_views.GitLabBranchesAPIView.as_view(), name="api_project_branches"),
    path("projects/<int:project_id>/tree/", api_views.GitLabFileTreeAPIView.as_view(), name="api_project_tree"),
    # Subscription management API
    path("subscriptions/", api_views.SubscriptionListAPIView.as_view(), name="api_subscription_list"),
    path("subscriptions/<int:subscription_id>/", api_views.SubscriptionDetailAPIView.as_view(), name="api_subscription_detail"),
    # Runner API (for CI/CD pipeline integration) - uses App Token auth, CSRF-exempt
    path("runner/changes/", api_views.runner_changes_api, name="api_runner_changes"),
]
