from browser.browser import BrowserManager
from backend.utils.logger import get_logger

logger = get_logger()


class LinkedInAgent:

    def __init__(self):

        self.browser = BrowserManager()

        self.page = None

    def start(self):

        self.page = self.browser.start()

    def open(self):

        logger.info("Opening LinkedIn")

        self.page.goto(
            "https://www.linkedin.com/"
        )

    def stop(self):

        self.browser.stop()