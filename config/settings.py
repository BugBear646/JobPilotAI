"""
==================================================
JobPilotAI Configuration
==================================================
Central configuration for the application.

DO NOT hardcode business logic elsewhere.
All configurable values should live here.
==================================================
"""

from pathlib import Path

# -------------------------------------------------
# Project Root
# -------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------
# Directories
# -------------------------------------------------

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

RESUME_DIR = ROOT_DIR / "resumes"

STORAGE_DIR = ROOT_DIR / "storage"

PROFILE_DIR = STORAGE_DIR / "browser_profile"

DOWNLOAD_DIR = STORAGE_DIR / "downloads"

SCREENSHOT_DIR = STORAGE_DIR / "screenshots"

CACHE_DIR = STORAGE_DIR / "cache"

# -------------------------------------------------
# LinkedIn
# -------------------------------------------------

LINKEDIN_HOME = "https://www.linkedin.com"

LINKEDIN_LOGIN = "https://www.linkedin.com/login"

LINKEDIN_JOBS = "https://www.linkedin.com/jobs"

# -------------------------------------------------
# Browser
# -------------------------------------------------

HEADLESS = False

SLOW_MO = 100

DEFAULT_TIMEOUT = 30000

# -------------------------------------------------
# Automation
# -------------------------------------------------

DEFAULT_MAX_APPLICATIONS = 50

ABSOLUTE_MAX_APPLICATIONS = 50

SCROLL_PAUSE = 2

CLICK_PAUSE = 1

# -------------------------------------------------
# Logging
# -------------------------------------------------

LOG_LEVEL = "INFO"

# -------------------------------------------------
# Create required folders automatically
# -------------------------------------------------

for folder in [
    DATA_DIR,
    LOG_DIR,
    RESUME_DIR,
    STORAGE_DIR,
    PROFILE_DIR,
    DOWNLOAD_DIR,
    SCREENSHOT_DIR,
    CACHE_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)