"""URL configuration for subscription app (web views)."""
from django.urls import path

from subscription import views

app_name = "subscription"

urlpatterns = [
    path("projects/", views.project_list, name="project_list"),
    path("projects/create/", views.project_create, name="project_create"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/<int:project_id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:project_id>/subscribe/", views.subscription_create, name="subscription_create"),
    path("my-subscriptions/", views.subscription_list, name="subscription_list"),
    path("subscriptions/<int:subscription_id>/delete/", views.subscription_delete, name="subscription_delete"),
]
