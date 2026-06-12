import time


class JobCollector:

    def __init__(self, page):

        self.page = page

    def collect(
        self,
        max_jobs=50,
    ):

        print("\nCollecting jobs...\n")

        self._wait_for_sidebar()

        container = self._get_scroll_container()

        jobs = {}
        previous_count = 0
        stagnant_rounds = 0

        while True:

            cards = self.page.locator(
                "div.job-card-container[data-job-id]"
            )

            count = cards.count()

            for i in range(count):

                try:

                    card = cards.nth(i)

                    job_id = card.get_attribute(
                        "data-job-id"
                    )

                    if not job_id:
                        continue

                    if job_id in jobs:
                        continue

                    jobs[job_id] = {
                        "job_id": job_id,
                        "element": card,
                    }

                except Exception:
                    continue

            print(
                f"Collected {len(jobs)} unique jobs..."
            )

            if len(jobs) >= max_jobs:

                break

            if len(jobs) == previous_count:

                stagnant_rounds += 1

            else:

                stagnant_rounds = 0

            if stagnant_rounds >= 3:

                print(
                    "\nNo more jobs detected.\n"
                )

                break

            previous_count = len(jobs)

            try:

                container.evaluate(
                    """
                    element => {
                        element.scrollBy(
                            0,
                            1200
                        );
                    }
                    """
                )

            except Exception:

                self.page.mouse.wheel(
                    0,
                    2000,
                )

            time.sleep(2)

        result = list(jobs.values())

        print("\n==============================")
        print(
            f"Total Jobs Collected : {len(result)}"
        )
        print("==============================\n")

        return result

    def _wait_for_sidebar(self):

        selectors = [
            "div.scaffold-layout__list",
            "ul.scaffold-layout__list-container",
            ".jobs-search-results-list",
        ]

        for selector in selectors:

            try:

                self.page.wait_for_selector(
                    selector,
                    timeout=5000,
                )

                return

            except Exception:

                pass

        raise Exception(
            "Unable to locate LinkedIn jobs list."
        )

    def _get_scroll_container(self):

        selectors = [
            "div.scaffold-layout__list",
            ".jobs-search-results-list",
            "body",
        ]

        for selector in selectors:

            try:

                locator = self.page.locator(
                    selector
                )

                if locator.count() > 0:
                    return locator.first

            except Exception:

                pass

        return self.page.locator("body")