"""URL configuration for core."""
from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("account/bind-username/", views.bind_username, name="bind_username"),
]
