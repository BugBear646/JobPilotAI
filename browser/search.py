import time


LOGIN_TIMEOUT = 600  # 10 minutes


def is_logged_in(page):
    """
    Returns True if the user is logged into LinkedIn.
    """

    try:

        url = page.url.lower()

        if "feed" in url:
            return True

        if "jobs" in url:
            return True

        if page.locator("input[placeholder='Search']").count() > 0:
            return True

        if page.locator("nav").count() > 0:
            return True

    except Exception:
        pass

    return False


def login(page):
    """
    Opens LinkedIn and waits until login is completed.
    """

    print("=" * 50)
    print("LinkedIn Login")
    print("=" * 50)

    page.goto(
        "https://www.linkedin.com/",
        wait_until="domcontentloaded",
    )

    page.wait_for_timeout(2000)

    if is_logged_in(page):

        print("\nAlready logged in.\n")
        return

    print("\nPlease login in the opened browser.\n")
    print("Waiting for login...\n")

    start = time.time()

    while True:

        if is_logged_in(page):

            print("Login detected!\n")
            return

        if time.time() - start > LOGIN_TIMEOUT:

            raise Exception(
                "Login timeout. Please restart and login again."
            )

        time.sleep(2)