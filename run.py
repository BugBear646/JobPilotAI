from browser.linkedin import LinkedInAgent


def main():

    agent = LinkedInAgent()

    try:

        agent.start()

        agent.open()

        input(
            "\n\nPress ENTER to close browser..."
        )

    finally:

        agent.stop()


if __name__ == "__main__":

    main()