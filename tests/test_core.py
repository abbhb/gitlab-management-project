"""Tests for the core app rename and URL namespace."""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.dev")
os.environ.setdefault("ENABLE_MOCK_LOGIN", "True")
os.environ.setdefault("BK_IAM_SKIP", "True")

from django.apps import apps
from django.test import SimpleTestCase
from django.urls import reverse


class CoreAppConfigTestCase(SimpleTestCase):
    """Ensure the renamed core app keeps compatibility-sensitive config."""

    def test_core_app_uses_professional_package_name(self):
        app_config = apps.get_app_config("home_application")

        self.assertEqual(app_config.name, "core")

    def test_core_url_namespace_resolves_expected_paths(self):
        self.assertEqual(reverse("core:index"), "/")
        self.assertEqual(reverse("core:bind_username"), "/account/bind-username/")
