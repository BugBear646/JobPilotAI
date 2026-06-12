from playwright.sync_api import sync_playwright

from config.settings import settings
from backend.utils.logger import get_logger


logger = get_logger()


class BrowserManager:

    def __init__(self):

        self.playwright = None

        self.browser = None

        self.context = None

        self.page = None

    def start(self):

        logger.info("Starting browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=settings.HEADLESS
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

        self.page.set_default_timeout(
            settings.TIMEOUT
        )

        logger.info("Browser started.")

        return self.page

    def stop(self):

        logger.info("Closing browser...")

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        logger.info("Browser closed.")