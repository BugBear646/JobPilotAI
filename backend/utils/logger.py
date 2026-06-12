import logging
from pathlib import Path

from config.settings import settings


# Create logs directory if it doesn't exist
Path(settings.LOG_DIR).mkdir(parents=True, exist_ok=True)


LOG_FILE = Path(settings.LOG_DIR) / "application.log"


logger = logging.getLogger("JobPilotAI")

logger.setLevel(logging.INFO)


# Avoid duplicate handlers
if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)


def get_logger():
    """
    Returns the global logger instance.

    Usage:

    from backend.utils.logger import get_logger

    logger = get_logger()

    logger.info("Hello")
    """

    return logger