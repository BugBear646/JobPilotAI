from pathlib import Path
from playwright.sync_api import sync_playwright

from config.settings import settings
from backend.utils.logger import get_logger

logger = get_logger()


class BrowserManager:

    def __init__(self):
        self.playwright = None
        self.context = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        profile_dir = (
            Path(settings.BASE_DIR)
            / "storage"
            / "browser_profile"
        )

        profile_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.context = (
            self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(profile_dir),
                headless=settings.HEADLESS,
            )
        )

        self.page = self.context.new_page()

        self.page.set_default_timeout(
            settings.TIMEOUT
        )

        return self.page

    def stop(self):

        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()