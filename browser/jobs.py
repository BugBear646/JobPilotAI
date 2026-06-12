"""
==================================================
Job Iterator

Responsibilities

- Read all visible job cards
- Click each job card
- Wait for right panel to load
- Check if Easy Apply exists
- Return valid jobs

==================================================
"""

from backend.utils.logger import get_logger

logger = get_logger()


class JobIterator:

    def __init__(self, page):

        self.page = page

    def get_job_cards(self):

        selectors = [
            "div.scaffold-layout__list li",
            "ul.jobs-search__results-list li",
            "li.jobs-search-results__list-item",
        ]

        for selector in selectors:

            try:

                self.page.wait_for_selector(
                    selector,
                    timeout=5000,
                )

                cards = self.page.locator(selector)

                count = cards.count()

                if count > 0:

                    logger.info(
                        f"Found {count} job cards."
                    )

                    return cards

            except Exception:

                continue

        return None

    def iterate(self, limit):

        cards = self.get_job_cards()

        if cards is None:

            logger.info("No jobs found.")

            return

        total = cards.count()

        logger.info(
            f"Processing {min(total, limit)} jobs..."
        )

        for i in range(min(total, limit)):

            card = cards.nth(i)

            try:

                card.scroll_into_view_if_needed()

                self.page.wait_for_timeout(1000)

                card.click()

                self.page.wait_for_timeout(3000)

                yield {
                    "index": i + 1,
                    "card": card,
                }

            except Exception as e:

                logger.info(
                    f"Skipping card {i+1}: {e}"
                )