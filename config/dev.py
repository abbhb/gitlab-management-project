"""
Development settings for bk_gitlab_sub project.
"""
import os

from config.default import *  # noqa: F401, F403

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Use SQLite for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),  # noqa: F405
    }
}

# In development, allow all CORS origins
CORS_ALLOW_ALL_ORIGINS = True

# Skip IAM checks during development
BK_IAM_SKIP = os.environ.get("BK_IAM_SKIP", "True").lower() == "true"

# Development-only: allow login without BlueKing SSO
# To test locally without BlueKing PaaS, set ENABLE_MOCK_LOGIN=True
ENABLE_MOCK_LOGIN = os.environ.get("ENABLE_MOCK_LOGIN", "False").lower() == "true"

# Override blueapps middleware if mock login is enabled
if ENABLE_MOCK_LOGIN:
    MIDDLEWARE = [m for m in MIDDLEWARE if "blueapps" not in m]  # noqa: F405
    MIDDLEWARE.append("home_application.middleware.MockLoginMiddleware")

# Static files served directly in development (same as default, explicitly set for clarity)
