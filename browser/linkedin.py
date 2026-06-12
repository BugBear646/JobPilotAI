from browser.browser import BrowserManager
from browser.search import LinkedInSearch
from backend.utils.logger import get_logger

logger = get_logger()


class LinkedInAgent:

    def __init__(self):
        self.browser = BrowserManager()
        self.page = None
        self.search_engine = None

    def start(self):
        self.page = self.browser.start()
        self.search_engine = LinkedInSearch(self.page)

    def open(self):
        self.page.goto("https://www.linkedin.com/login")

    def wait_for_login(self):

        print("\nPlease login in the opened browser...")

        while True:

            if "/feed" in self.page.url:

                print("\nLogin detected!")

                break

            self.page.wait_for_timeout(1000)

    def search(self, keyword, location=""):

        self.search_engine.search(
            keyword,
            location,
        )

    def stop(self):

        self.browser.stop()