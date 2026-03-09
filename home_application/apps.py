"""AppConfig for home_application."""
from django.apps import AppConfig


class HomeApplicationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home_application"
    verbose_name = "首页"
