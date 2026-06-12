from browser.linkedin import LinkedInAgent


def main():
    agent = LinkedInAgent()

    try:
        # Start browser
        agent.start()

        # Open LinkedIn login page
        agent.open()

        # Wait until login is completed
        agent.wait_for_login()

        print("\n===================================")
        print("Searching for jobs...")
        print("Keyword : Product Manager")
        print("Location: India")
        print("===================================\n")

        # Search jobs
        agent.search(
            keyword="Product Manager",
            location="India",
        )

        # Debug information
        print("\nNavigation successful!")
        print(f"Current URL  : {agent.page.url}")
        print(f"Page Title   : {agent.page.title()}")

        input("\nPress ENTER to close browser...")

    except Exception as e:
        print("\n===================================")
        print("ERROR")
        print("===================================")
        print(e)

    finally:
        agent.stop()


if __name__ == "__main__":
    main()
