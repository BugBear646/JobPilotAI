from urllib.parse import quote_plus
from playwright.sync_api import sync_playwright

from browser.login import login
from browser.jobs import JobCrawler


MAX_LIMIT = 50


def get_inputs():

    print("\n==============================")
    print(" JobPilotAI ")
    print("==============================\n")

    role = input(
        "Target Role (Example: Product Manager): "
    ).strip()

    while not role:
        role = input(
            "Role cannot be empty: "
        ).strip()

    location = input(
        "Location (Example: India): "
    ).strip()

    if not location:
        location = "India"

    try:
        maximum = int(
            input(
                f"Maximum Applications (1-{MAX_LIMIT}): "
            )
        )
    except:
        maximum = 20

    maximum = max(1, minimum(maximum, MAX_LIMIT))

    return role, location, maximum


def minimum(a, b):
    return a if a < b else b


def build_url(role, location):

    role = quote_plus(role)
    location = quote_plus(location)

    return (
        "https://www.linkedin.com/jobs/search/"
        f"?f_AL=true"
        f"&keywords={role}"
        f"&location={location}"
    )


def main():

    role, location, maximum = get_inputs()

    url = build_url(role, location)

    print("\n================================")
    print("Opening LinkedIn Search")
    print("================================\n")

    print(url)
    print()

    with sync_playwright() as p:

        browser = p.chromium.launch_persistent_context(
            user_data_dir="storage/browser_profile",
            headless=False,
        )

        page = browser.new_page()

        login(page)

        page.goto(
            url,
            wait_until="domcontentloaded",
        )

        page.wait_for_timeout(5000)

        crawler = JobCrawler(page)

        crawler.load_all_jobs(
            target=maximum
        )

        crawler.visit_jobs()

        print("\n================================")
        print("Finished")
        print("================================\n")

        input("Press ENTER to exit...")

        browser.close()


if __name__ == "__main__":
    main()