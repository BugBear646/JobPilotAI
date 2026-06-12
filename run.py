"""
==================================================
JobPilotAI

Main Entry Point

Flow

1. Start Browser
2. Detect/Login LinkedIn
3. Ask User Preferences
4. Open Easy Apply Search
5. Ready for Job Processing

==================================================
"""

from browser.browser import BrowserManager
from browser.login import LoginManager
from browser.search import SearchManager


def banner():

    print("\n")
    print("=" * 60)
    print("                JobPilotAI")
    print("=" * 60)
    print("LinkedIn Easy Apply Automation")
    print("=" * 60)
    print()


def main():

    banner()

    browser = BrowserManager()

    page = browser.start()

    try:

        # ---------------------------------
        # Login
        # ---------------------------------

        login = LoginManager(page)

        login.login()

        # ---------------------------------
        # User Preferences
        # ---------------------------------

        search = SearchManager(page)

        config = search.get_user_preferences()

        print("\n")
        print("=" * 60)
        print("Configuration")
        print("=" * 60)
        print(f"Roles              : {config['roles']}")
        print(f"Location           : {config['location']}")
        print(
            f"Maximum Apply      : {config['max_applications']}"
        )
        print("=" * 60)
        print()

        # ---------------------------------
        # Search
        # ---------------------------------

        search.open_search(
            config["roles"],
            config["location"],
        )

        print("\n")
        print("=" * 60)
        print("Easy Apply search loaded successfully.")
        print("Next step: Job Iterator")
        print("=" * 60)
        print()

        input(
            "Press ENTER to close browser..."
        )

    finally:

        browser.stop()


if __name__ == "__main__":

    main()