"""
==================================================
JobPilotAI Login Manager
==================================================

Responsibilities:

- Open LinkedIn
- Detect existing login
- Wait for manual login if required
- Return only after login succeeds

==================================================
"""

import time

from config.settings import (
    LINKEDIN_HOME,
)


class LoginManager:

    def __init__(self, page):

        self.page = page

    def login(self):

        print("\n====================================")
        print("Opening LinkedIn...")
        print("====================================\n")

        self.page.goto(
            LINKEDIN_HOME,
            wait_until="domcontentloaded",
        )

        self.page.wait_for_timeout(3000)

        if self.is_logged_in():

            print("✅ Existing session detected.\n")

            return

        print("====================================")
        print("Please login to LinkedIn.")
        print("Automation will continue automatically.")
        print("====================================\n")

        while True:

            if self.is_logged_in():

                print("\n✅ Login detected!\n")

                break

            time.sleep(2)

    def is_logged_in(self):

        current_url = self.page.url.lower()

        if "feed" in current_url:
            return True

        try:

            if self.page.locator(
                "input[placeholder='Search']"
            ).count() > 0:

                return True

        except:

            pass

        try:

            if self.page.locator(
                "input[placeholder='Search by title, skill, or company']"
            ).count() > 0:

                return True

        except:

            pass

        try:

            if self.page.locator(
                "nav"
            ).count() > 0 and "login" not in current_url:

                return True

        except:

            pass

        return False