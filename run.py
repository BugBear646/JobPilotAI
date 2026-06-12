from browser.apply import JobApplyAgent

MAX_APPLICATIONS = 50


def banner():
    print("\n" + "=" * 50)
    print("                 JobPilotAI")
    print("=" * 50)


def choose_mode():
    print("\nSelect Mode\n")
    print("1. Use LinkedIn Search URL")
    print("2. Create Search\n")

    while True:
        choice = input("> ").strip()

        if choice in ["1", "2"]:
            return choice

        print("\nPlease enter 1 or 2.\n")


def ask_search_url():
    print("\nPaste LinkedIn Jobs URL\n")

    while True:
        url = input("> ").strip()

        if url:
            return url

        print("\nURL cannot be empty.\n")


def ask_role():
    print("\nTarget Job Role\n")

    while True:
        role = input("> ").strip()

        if role:
            return role

        print("\nRole cannot be empty.\n")


def ask_location():
    print("\nLocation\n")

    while True:
        location = input("> ").strip()

        if location:
            return location

        print("\nLocation cannot be empty.\n")


def ask_max_applications():
    print(f"\nMaximum Applications (Max {MAX_APPLICATIONS})\n")

    while True:

        value = input("> ").strip()

        try:

            value = int(value)

            if value < 1:
                print("\nValue must be greater than 0.\n")
                continue

            if value > MAX_APPLICATIONS:
                print(
                    f"\nMaximum allowed is {MAX_APPLICATIONS}. Using {MAX_APPLICATIONS}."
                )
                value = MAX_APPLICATIONS

            return value

        except ValueError:

            print("\nPlease enter a valid number.\n")


def build_config():

    mode = choose_mode()

    config = {}

    if mode == "1":

        config["mode"] = "url"
        config["search_url"] = ask_search_url()

    else:

        config["mode"] = "search"
        config["role"] = ask_role()
        config["location"] = ask_location()

    config["max_applications"] = ask_max_applications()

    return config


def print_summary(config):

    print("\n" + "=" * 50)
    print("Configuration")
    print("=" * 50)

    if config["mode"] == "url":

        print(f"Mode                 : Search URL")
        print(f"Search URL           : {config['search_url']}")

    else:

        print(f"Mode                 : Create Search")
        print(f"Target Role          : {config['role']}")
        print(f"Location             : {config['location']}")

    print("Easy Apply           : Yes")
    print(f"Maximum Applications : {config['max_applications']}")

    print("\nStarting Automation...\n")


def main():

    banner()

    config = build_config()

    print_summary(config)

    agent = JobApplyAgent(config)

    agent.run()


if __name__ == "__main__":
    main()