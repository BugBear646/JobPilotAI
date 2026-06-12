from pathlib import Path
from dotenv import load_dotenv
import os

# -----------------------------
# Project Root
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Load .env
# -----------------------------

load_dotenv(BASE_DIR / ".env")


class Settings:
    """
    Global configuration for JobPilotAI.
    Import this object anywhere in the project.

    Example:
        from config.settings import settings
        print(settings.OPENAI_API_KEY)
    """

    # =========================
    # Project
    # =========================

    PROJECT_NAME = "JobPilotAI"

    VERSION = "0.1.0"

    DEBUG = True

    # =========================
    # Paths
    # =========================

    BASE_DIR = BASE_DIR

    DATABASE_DIR = BASE_DIR / "database"

    RESUME_DIR = BASE_DIR / "resumes"

    LOG_DIR = BASE_DIR / "logs"

    PROMPT_DIR = BASE_DIR / "prompts"

    STORAGE_DIR = BASE_DIR / "storage"

    CACHE_DIR = STORAGE_DIR / "cache"

    DOWNLOAD_DIR = STORAGE_DIR / "downloads"

    SCREENSHOT_DIR = STORAGE_DIR / "screenshots"

    # =========================
    # Database
    # =========================

    DATABASE_PATH = DATABASE_DIR / "jobpilot.db"

    # =========================
    # OpenAI
    # =========================

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    MODEL = "gpt-5.5"

    # =========================
    # User Details
    # =========================

    FULL_NAME = os.getenv("FULL_NAME", "")

    EMAIL = os.getenv("EMAIL", "")

    PHONE = os.getenv("PHONE", "")

    LINKEDIN = os.getenv("LINKEDIN", "")

    GITHUB = os.getenv("GITHUB", "")

    CURRENT_LOCATION = os.getenv("CURRENT_LOCATION", "")

    NOTICE_PERIOD = os.getenv("NOTICE_PERIOD", "")

    CURRENT_CTC = os.getenv("CURRENT_CTC", "")

    EXPECTED_CTC = os.getenv("EXPECTED_CTC", "")

    # =========================
    # Application Config
    # =========================

    MAX_APPLICATIONS = 200

    HEADLESS = False

    TIMEOUT = 30000


settings = Settings()