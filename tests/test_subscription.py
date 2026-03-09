"""
Unit tests for subscription matching logic and core business functions.
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.dev")
os.environ.setdefault("ENABLE_MOCK_LOGIN", "True")
os.environ.setdefault("BK_IAM_SKIP", "True")

from django.test import TestCase
from django.contrib.auth import get_user_model

from home_application.models import UserProfile
from subscription.models import GitLabProject, Subscription
from subscription.utils import match_changed_files_to_subscriptions

User = get_user_model()


class SubscriptionMatchingTestCase(TestCase):
    """Tests for the path matching logic."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create(username="test_user", is_active=True)
        self.profile = UserProfile.objects.create(
            user=self.user, enterprise_username="test_enterprise"
        )
        self.project = GitLabProject.objects.create(
            name="Test Project",
            gitlab_url="https://gitlab.example.com",
            gitlab_project_id=1,
            gitlab_token="test_token",
            default_branch="main",
            created_by=self.user,
        )

    def _create_subscription(self, path, path_type, branch="main"):
        return Subscription.objects.create(
            user=self.user,
            project=self.project,
            path=path,
            path_type=path_type,
            branch=branch,
        )

    def test_directory_subscription_matches_files_in_directory(self):
        """Test that a directory subscription matches files under it."""
        self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY)
        changed_files = ["src/main.py", "src/utils.py", "src/models/user.py"]
        subscriptions = Subscription.objects.filter(project=self.project).select_related(
            "user", "user__profile"
        )
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertIn("test_enterprise", result)
        self.assertIn("src/main.py", result["test_enterprise"])
        self.assertIn("src/utils.py", result["test_enterprise"])
        self.assertIn("src/models/user.py", result["test_enterprise"])

    def test_directory_subscription_does_not_match_outside(self):
        """Test that a directory subscription does not match files outside it."""
        self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY)
        changed_files = ["docs/README.md", "tests/test_main.py"]
        subscriptions = Subscription.objects.filter(project=self.project).select_related(
            "user", "user__profile"
        )
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertNotIn("test_enterprise", result)

    def test_file_subscription_exact_match_only(self):
        """Test that a file subscription only matches the exact file."""
        self._create_subscription("README.md", Subscription.PATH_TYPE_FILE)
        changed_files = ["README.md", "src/README.md", "docs/README.md"]
        subscriptions = Subscription.objects.filter(project=self.project).select_related(
            "user", "user__profile"
        )
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertIn("test_enterprise", result)
        self.assertIn("README.md", result["test_enterprise"])
        # Only exact match - subdirectory files should not match
        self.assertNotIn("src/README.md", result["test_enterprise"])
        self.assertNotIn("docs/README.md", result["test_enterprise"])

    def test_multiple_subscriptions_aggregate_changes(self):
        """Test that multiple subscriptions for one user aggregate changes."""
        self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY)
        self._create_subscription("README.md", Subscription.PATH_TYPE_FILE)
        changed_files = ["src/main.py", "README.md", "docs/guide.md"]
        subscriptions = Subscription.objects.filter(project=self.project).select_related(
            "user", "user__profile"
        )
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertIn("test_enterprise", result)
        self.assertIn("src/main.py", result["test_enterprise"])
        self.assertIn("README.md", result["test_enterprise"])
        self.assertNotIn("docs/guide.md", result["test_enterprise"])

    def test_no_matching_subscriptions_returns_empty(self):
        """Test that no matching subscriptions returns an empty dict."""
        self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY)
        changed_files = ["docs/guide.md", "tests/test.py"]
        subscriptions = Subscription.objects.filter(project=self.project).select_related(
            "user", "user__profile"
        )
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertEqual(result, {})

    def test_branch_filter_by_target_branch(self):
        """Test that subscriptions on different branches are properly handled."""
        self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY, branch="main")
        self._create_subscription("docs/", Subscription.PATH_TYPE_DIRECTORY, branch="develop")
        changed_files = ["src/main.py", "docs/guide.md"]

        # Filter for 'main' branch only
        subscriptions = Subscription.objects.filter(
            project=self.project, branch="main"
        ).select_related("user", "user__profile")
        result = match_changed_files_to_subscriptions(changed_files, subscriptions)
        self.assertIn("test_enterprise", result)
        self.assertIn("src/main.py", result["test_enterprise"])
        # docs/ subscription is on develop branch, should not match
        self.assertNotIn("docs/guide.md", result["test_enterprise"])

    def test_subscription_matches_path_method_directory(self):
        """Test the Subscription.matches_path method for directories."""
        sub = self._create_subscription("src/", Subscription.PATH_TYPE_DIRECTORY)
        self.assertTrue(sub.matches_path("src/main.py"))
        self.assertTrue(sub.matches_path("src/models/user.py"))
        self.assertFalse(sub.matches_path("docs/readme.md"))
        self.assertFalse(sub.matches_path("srcs/main.py"))

    def test_subscription_matches_path_method_file(self):
        """Test the Subscription.matches_path method for files."""
        sub = self._create_subscription("README.md", Subscription.PATH_TYPE_FILE)
        self.assertTrue(sub.matches_path("README.md"))
        self.assertFalse(sub.matches_path("docs/README.md"))
        self.assertFalse(sub.matches_path("README.md.bak"))


class UserProfileTestCase(TestCase):
    """Tests for UserProfile model."""

    def test_enterprise_username_unique(self):
        """Test that enterprise usernames must be unique."""
        from django.db import IntegrityError

        user1 = User.objects.create(username="user1", is_active=True)
        user2 = User.objects.create(username="user2", is_active=True)
        UserProfile.objects.create(user=user1, enterprise_username="john")
        with self.assertRaises(IntegrityError):
            UserProfile.objects.create(user=user2, enterprise_username="john")

    def test_str_representation(self):
        """Test UserProfile string representation."""
        user = User.objects.create(username="test_user2", is_active=True)
        profile = UserProfile.objects.create(user=user, enterprise_username="john_doe")
        self.assertEqual(str(profile), "test_user2 -> john_doe")


class RunnerAPITestCase(TestCase):
    """Tests for the Runner API endpoint."""

    def setUp(self):
        """Set up test data."""
        from django.conf import settings

        self.user = User.objects.create(username="api_test_user", is_active=True, is_superuser=True, is_staff=True)
        self.profile = UserProfile.objects.create(
            user=self.user, enterprise_username="api_test_enterprise"
        )
        self.project = GitLabProject.objects.create(
            name="API Test Project",
            gitlab_url="https://gitlab.example.com",
            gitlab_project_id=42,
            gitlab_token="test_token",
            default_branch="main",
            created_by=self.user,
        )
        Subscription.objects.create(
            user=self.user,
            project=self.project,
            path="src/",
            path_type=Subscription.PATH_TYPE_DIRECTORY,
            branch="main",
        )
        # Create runner user (no UserProfile needed - API paths are exempt from binding)
        self.runner_user = User.objects.create(username="__runner_test__", is_active=True)

    def test_runner_api_requires_authentication(self):
        """Test that the runner API returns 403 for unauthenticated requests (without mock login)."""
        from django.test import override_settings
        from config.dev import MIDDLEWARE as DEV_MIDDLEWARE

        # Remove MockLoginMiddleware for this test to test actual auth behavior
        middleware_without_mock = [m for m in DEV_MIDDLEWARE if "MockLogin" not in m]

        with override_settings(MIDDLEWARE=middleware_without_mock):
            response = self.client.post(
                "/api/runner/changes/",
                data={"project_id": self.project.id, "changed_files": ["src/main.py"]},
                content_type="application/json",
            )
        # Without authentication (no session, no app token), should be 403
        self.assertIn(response.status_code, [403, 401])

    def test_runner_api_with_logged_in_user(self):
        """Test the runner API works for authenticated user."""
        self.client.force_login(self.runner_user, backend="django.contrib.auth.backends.ModelBackend")
        response = self.client.post(
            "/api/runner/changes/",
            data={
                "project_id": self.project.id,
                "changed_files": ["src/main.py", "docs/readme.md"],
                "target_branch": "main",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["result"])
        self.assertIn("api_test_enterprise", data["data"])
        self.assertIn("src/main.py", data["data"]["api_test_enterprise"])
        self.assertNotIn("docs/readme.md", data["data"]["api_test_enterprise"])

    def test_runner_api_invalid_project(self):
        """Test the runner API with invalid project ID."""
        self.client.force_login(self.runner_user, backend="django.contrib.auth.backends.ModelBackend")
        response = self.client.post(
            "/api/runner/changes/",
            data={"project_id": 99999, "changed_files": ["src/main.py"]},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)

    def test_runner_api_empty_changed_files_validation(self):
        """Test the runner API with empty changed files list."""
        self.client.force_login(self.runner_user, backend="django.contrib.auth.backends.ModelBackend")
        response = self.client.post(
            "/api/runner/changes/",
            data={"project_id": self.project.id, "changed_files": []},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_runner_api_no_matching_subscriptions(self):
        """Test the runner API when no subscriptions match the changed files."""
        self.client.force_login(self.runner_user, backend="django.contrib.auth.backends.ModelBackend")
        response = self.client.post(
            "/api/runner/changes/",
            data={
                "project_id": self.project.id,
                "changed_files": ["docs/guide.md", "tests/test.py"],
                "target_branch": "main",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["result"])
        self.assertEqual(data["data"], {})
