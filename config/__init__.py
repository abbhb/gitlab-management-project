"""
Django settings module for bk_gitlab_sub project.

Exposes base settings so blueapps.conf can discover BASE_DIR and RUN_VER.
"""
# Import base settings to expose them at the package level (required by blueapps.conf)
from config.default import *  # noqa: F401, F403
