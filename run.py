from browser.linkedin import LinkedInAgent


def main():

    agent = LinkedInAgent()

    try:

        agent.start()

        agent.open()

        agent.wait_for_login()

        print(
            "\nSearching Easy Apply jobs...\n"
        )

        agent.search(
            keyword="Product Manager",
            location="India",
        )

        job_ids = agent.collect_jobs(
            limit=200
        )

        print()

        print("=" * 80)

        print(
            f"Collected {len(job_ids)} jobs"
        )

        print("=" * 80)

        for i, job in enumerate(
            job_ids,
            1,
        ):

            print(
                f"{i}. {job}"
            )

    finally:

        input(
            "\nPress ENTER to close browser..."
        )

        agent.stop()


if __name__ == "__main__":
    main()