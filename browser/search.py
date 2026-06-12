from urllib.parse import quote_plus

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from backend.utils.logger import get_logger

logger = get_logger()


class LinkedInSearch:
    """
    Handles LinkedIn job search navigation.
    """

    def __init__(self, page):
        self.page = page

    def search(
        self,
        keyword: str,
        location: str = "",
    ):

        keyword = quote_plus(keyword.strip())
        location = quote_plus(location.strip())

        url = (
            "https://www.linkedin.com/jobs/search/"
            f"?keywords={keyword}"
            f"&location={location}"
        )

        logger.info(f"Opening Jobs URL: {url}")

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        # Wait until the page settles a bit
        self.page.wait_for_timeout(3000)

        # Try waiting for a jobs-related element
        selectors = [
            "div.jobs-search-results-list",
            "ul.jobs-search__results-list",
            "div.scaffold-layout__list",
            "main",
        ]

        loaded = False

        for selector in selectors:
            try:
                self.page.wait_for_selector(
                    selector,
                    timeout=5000,
                )
                logger.info(
                    f"Found selector: {selector}"
                )
                loaded = True
                break
            except PlaywrightTimeoutError:
                continue

        if not loaded:
            logger.warning(
                "Jobs container not found. Continuing anyway."
            )

        logger.info(
            f"Current URL: {self.page.url}"
        )

        logger.info(
            f"Page title: {self.page.title()}"
        )

        return self.page