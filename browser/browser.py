"""
==================================================
JobPilotAI Browser Manager
==================================================

Responsible for:

- Starting Playwright
- Creating persistent browser profile
- Reusing LinkedIn login session
- Returning active page
- Gracefully closing browser

==================================================
"""

from playwright.sync_api import sync_playwright

from config.settings import (
    PROFILE_DIR,
    HEADLESS,
    SLOW_MO,
)

from config.constants import (
    DEFAULT_TIMEOUT,
    USER_AGENT,
)


class BrowserManager:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = (
            self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE_DIR),
                headless=HEADLESS,
                slow_mo=SLOW_MO,
                viewport={
                    "width": 1440,
                    "height": 900,
                },
                user_agent=USER_AGENT,
            )
        )

        self.browser.set_default_timeout(
            DEFAULT_TIMEOUT
        )

        pages = self.browser.pages

        if pages:
            self.page = pages[0]
        else:
            self.page = self.browser.new_page()

        return self.page

    def get_page(self):

        return self.page

    def stop(self):

        try:

            if self.browser:

                self.browser.close()

        finally:

            if self.playwright:

                self.playwright.stop()