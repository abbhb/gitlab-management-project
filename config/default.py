"""
Default/base Django settings for bk_gitlab_sub project.
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BlueKing App information
BK_APP_CODE = os.environ.get("APP_CODE", os.environ.get("BKPAAS_APP_ID", "bk_gitlab_sub"))
BK_APP_SECRET = os.environ.get("SECRET_KEY", os.environ.get("BKPAAS_APP_SECRET", ""))

# Alias used by blueapps.conf.default_settings
APP_CODE = BK_APP_CODE
SECRET_KEY_BK = BK_APP_SECRET

# Auth user model - uses blueapps custom user model
AUTH_USER_MODEL = "account.User"

# BlueKing PaaS environment variables
BK_PAAS_HOST = os.environ.get("BK_PAAS_HOST", os.environ.get("BKPAAS_URL", "http://paas.example.com"))
BK_LOGIN_URL = os.environ.get("BK_LOGIN_URL", BK_PAAS_HOST + "/login")
BK_LOGIN_INNER_URL = os.environ.get("BK_LOGIN_INNER_URL", BK_PAAS_HOST + "/login")
BK_IAM_HOST = os.environ.get("BK_IAM_HOST", "http://bkiam.example.com")
BK_IAM_SYSTEM_ID = BK_APP_CODE

# BlueKing platform version: "open" for community edition, "ieod" for internal edition
RUN_VER = os.environ.get("RUN_VER", "open")

# BlueKing initial superuser (required by blueapps migrations)
INIT_SUPERUSER = []


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "change-me-in-production-please")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # BlueKing
    "blueapps.account",
    "blueapps.utils",
    # Third party
    "rest_framework",
    "corsheaders",
    # Project apps
    "home_application",
    "subscription",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # BlueKing login middleware
    "blueapps.account.middlewares.LoginRequiredMiddleware",
    # Enterprise username binding middleware
    "home_application.middleware.EnterpriseUsernameBindingMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
                "home_application.context_processors.bk_context",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# Authentication backends - BlueKing SSO
# Note: In production with blueapps installed, use the appropriate site backend.
# For 'open' version: bk_token needs to be installed and use:
#   "blueapps.account.backends.UserBackend"
# For JWT-based auth:
#   "blueapps.account.backends.BkJwtBackend"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# BlueKing login configuration
LOGIN_URL = BK_LOGIN_URL

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Session settings
SESSION_COOKIE_NAME = "bk_token"
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# Cache configuration
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "default",
    },
    "login_db": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "django_cache",
    },
}

# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "subscription.authentication.AppTokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "EXCEPTION_HANDLER": "subscription.utils.custom_exception_handler",
}

# CORS settings (for frontend development)
CORS_ALLOWED_ORIGINS = []
CORS_ALLOW_CREDENTIALS = True

# BlueKing IAM settings
BK_IAM_SKIP = os.environ.get("BK_IAM_SKIP", "False").lower() == "true"

# GitLab default settings
GITLAB_DEFAULT_URL = os.environ.get("GITLAB_DEFAULT_URL", "https://gitlab.com")

# Runner API token for CI/CD script authentication
RUNNER_API_TOKEN = os.environ.get("RUNNER_API_TOKEN", "")

# Logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "subscription": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "home_application": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
