"""
==================================================
JobPilotAI

Main Entry Point

Flow

1. Start Browser
2. Login to LinkedIn
3. Ask User Preferences
4. Open Easy Apply Search
5. Iterate through Jobs

==================================================
"""

from browser.browser import BrowserManager
from browser.login import LoginManager
from browser.search import SearchManager
from browser.jobs import JobIterator


def banner():

    print("\n")
    print("=" * 60)
    print("                    JobPilotAI")
    print("=" * 60)
    print("         LinkedIn Easy Apply Automation")
    print("=" * 60)
    print()


def main():

    banner()

    browser = BrowserManager()

    page = browser.start()

    try:

        # ----------------------------------------
        # Login
        # ----------------------------------------

        login = LoginManager(page)

        login.login()

        # ----------------------------------------
        # User Configuration
        # ----------------------------------------

        search = SearchManager(page)

        config = search.get_user_preferences()

        print("\n")
        print("=" * 60)
        print("Configuration")
        print("=" * 60)
        print(f"Roles              : {config['roles']}")
        print(f"Location           : {config['location']}")
        print(f"Maximum Apply      : {config['max_applications']}")
        print("=" * 60)
        print()

        # ----------------------------------------
        # Open LinkedIn Search
        # ----------------------------------------

        search.open_search(
            config["roles"],
            config["location"],
        )

        print("\n")
        print("=" * 60)
        print("Starting Job Iterator")
        print("=" * 60)
        print()

        # ----------------------------------------
        # Iterate Jobs
        # ----------------------------------------

        iterator = JobIterator(page)

        visited = 0

        for job in iterator.iterate(
            config["max_applications"]
        ):

            visited += 1

            print(
                f"Visited Job #{visited}"
            )

        print("\n")
        print("=" * 60)
        print(f"Finished visiting {visited} jobs")
        print("=" * 60)

        input(
            "\nPress ENTER to close browser..."
        )

    finally:

        browser.stop()


if __name__ == "__main__":
    main()