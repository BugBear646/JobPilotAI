"""
==================================================
JobPilotAI Search Manager
==================================================

Responsibilities

- Ask user for target role(s)
- Ask user for preferred location
- Ask user for maximum applications
- Build LinkedIn Easy Apply search URL
- Open search page

==================================================
"""

from urllib.parse import quote_plus

from config.settings import LINKEDIN_JOBS
from config.constants import MAX_APPLICATIONS


class SearchManager:

    def __init__(self, page):

        self.page = page

    def get_user_preferences(self):

        print("\n======================================")
        print("        JobPilotAI Configuration")
        print("======================================\n")

        while True:

            roles = input(
                "Target Role(s)\n"
                "(comma separated)\n\n> "
            ).strip()

            if roles:
                break

            print("\nRole is mandatory.\n")

        while True:

            location = input(
                "\nPreferred Location\n\n> "
            ).strip()

            if location:
                break

            print("\nLocation is mandatory.\n")

        while True:

            value = input(
                f"\nMaximum Applications (1-{MAX_APPLICATIONS})\n\n> "
            ).strip()

            try:

                value = int(value)

                if value < 1:
                    raise ValueError

                if value > MAX_APPLICATIONS:

                    print(
                        f"\nMaximum allowed is {MAX_APPLICATIONS}. "
                        f"Using {MAX_APPLICATIONS}.\n"
                    )

                    value = MAX_APPLICATIONS

                break

            except:

                print("\nPlease enter a valid number.\n")

        return {
            "roles": roles,
            "location": location,
            "max_applications": value,
        }

    def open_search(self, roles, location):

        keywords = quote_plus(roles)

        location = quote_plus(location)

        url = (
            f"{LINKEDIN_JOBS}/search/"
            f"?f_AL=true"
            f"&keywords={keywords}"
            f"&location={location}"
        )

        print("\n======================================")
        print("Opening LinkedIn Search")
        print("======================================")
        print(url)
        print()

        self.page.goto(
            url,
            wait_until="domcontentloaded",
        )

        self.page.wait_for_timeout(5000)