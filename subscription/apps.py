"""AppConfig for subscription app."""
from django.apps import AppConfig


class SubscriptionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "subscription"
    verbose_name = "订阅管理"
