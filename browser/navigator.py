from playwright.sync_api import TimeoutError

from backend.utils.logger import get_logger

logger = get_logger()


class Navigator:
    """
    Handles navigation inside LinkedIn Easy Apply popup.
    """

    def __init__(self, page):
        self.page = page

    def click_next(self):
        selectors = [
            "button[aria-label='Continue to next step']",
            "button[aria-label='Next']",
            "button:has-text('Next')",
        ]

        for selector in selectors:
            try:
                button = self.page.locator(selector).first

                if button.is_visible(timeout=1000):
                    logger.info("Clicked Next")
                    button.click()
                    self.page.wait_for_timeout(1000)
                    return True

            except Exception:
                pass

        return False

    def click_review(self):
        selectors = [
            "button[aria-label='Review your application']",
            "button:has-text('Review')",
        ]

        for selector in selectors:
            try:
                button = self.page.locator(selector).first

                if button.is_visible(timeout=1000):
                    logger.info("Clicked Review")
                    button.click()
                    self.page.wait_for_timeout(1000)
                    return True

            except Exception:
                pass

        return False

    def click_submit(self):
        selectors = [
            "button[aria-label='Submit application']",
            "button:has-text('Submit application')",
            "button:has-text('Submit')",
        ]

        for selector in selectors:
            try:
                button = self.page.locator(selector).first

                if button.is_visible(timeout=1000):
                    logger.info("Submitting application")
                    button.click()
                    self.page.wait_for_timeout(2000)
                    return True

            except Exception:
                pass

        return False

    def process(self):
        """
        Navigate until submission page.
        Returns:
            "submitted"
            "review"
            "next"
            "stopped"
        """

        while True:

            if self.click_next():
                continue

            if self.click_review():
                continue

            if self.click_submit():
                return "submitted"

            logger.info("No Next/Review/Submit button found.")
            return "stopped"