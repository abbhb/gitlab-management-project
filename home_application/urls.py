"""URL configuration for home_application."""
from django.urls import path

from home_application import views

app_name = "home_application"

urlpatterns = [
    path("", views.index, name="index"),
    path("account/bind-username/", views.bind_username, name="bind_username"),
]
