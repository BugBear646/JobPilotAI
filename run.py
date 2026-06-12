from browser.linkedin import LinkedInAgent
from browser.apply import ApplyEngine


def main():

    print("\n" + "=" * 50)
    print("JobPilotAI")
    print("=" * 50)

    agent = LinkedInAgent()

    try:

        # -----------------------
        # Start Browser
        # -----------------------

        agent.start()

        # -----------------------
        # Login
        # -----------------------

        agent.login()

        # -----------------------
        # Ask User Inputs
        # -----------------------

        print()

        job_url = input(
            "Paste LinkedIn Jobs Search URL:\n> "
        ).strip()

        while job_url == "":
            job_url = input(
                "URL cannot be empty.\n> "
            ).strip()

        print()

        max_applications = input(
            "Maximum applications (Max 50): "
        ).strip()

        if max_applications == "":
            max_applications = 10

        max_applications = int(max_applications)

        max_applications = min(
            max(
                max_applications,
                1,
            ),
            50,
        )

        print()

        resume_path = input(
            "Resume path (Press Enter to use latest): "
        ).strip()

        if resume_path == "":
            resume_path = None

        # -----------------------
        # Profile
        # -----------------------

        profile = {
            "phone": "",
            "email": "",
            "city": "",
            "notice_period": "",
            "current_ctc": "",
            "expected_ctc": "",
            "linkedin": "",
            "github": "",
            "portfolio": "",
        }

        # -----------------------
        # Open Search URL
        # -----------------------

        print("\nOpening Jobs Page...\n")

        agent.page.goto(
            job_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        agent.page.wait_for_timeout(5000)

        # -----------------------
        # Apply Engine
        # -----------------------

        engine = ApplyEngine(
            page=agent.page,
            profile=profile,
            resume_path=resume_path,
            max_applications=max_applications,
        )

        engine.start()

        print("\n")
        print("=" * 50)
        print("Automation Finished")
        print("=" * 50)

        input(
            "\nPress ENTER to close browser..."
        )

    finally:

        agent.stop()


if __name__ == "__main__":
    main()