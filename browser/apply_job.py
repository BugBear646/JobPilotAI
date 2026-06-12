import time


class JobApplier:

    def __init__(self, page):

        self.page = page

    def open_job(self, job):

        try:

            print("=" * 60)
            print(f"Opening Job : {job['job_id']}")
            print("=" * 60)

            job["element"].scroll_into_view_if_needed()

            time.sleep(1)

            job["element"].click(
                timeout=5000,
                force=True,
            )

            self._wait_for_details()

            easy_apply = self.has_easy_apply()

            if easy_apply:

                print("Easy Apply : YES\n")

            else:

                print("Easy Apply : NO\n")

            return easy_apply

        except Exception as e:

            print(f"Failed to open job: {e}\n")

            return False

    def has_easy_apply(self):

        selectors = [

            "button.jobs-apply-button",

            "button[aria-label*='Easy Apply']",

            "button:has-text('Easy Apply')",

            ".jobs-apply-button",

        ]

        for selector in selectors:

            try:

                locator = self.page.locator(selector)

                if locator.count() > 0:

                    if locator.first.is_visible():

                        return True

            except Exception:

                pass

        return False

    def click_easy_apply(self):

        selectors = [

            "button.jobs-apply-button",

            "button[aria-label*='Easy Apply']",

            "button:has-text('Easy Apply')",

            ".jobs-apply-button",

        ]

        for selector in selectors:

            try:

                locator = self.page.locator(selector)

                if locator.count() == 0:
                    continue

                button = locator.first

                if not button.is_visible():
                    continue

                print("Clicking Easy Apply...\n")

                button.click()

                time.sleep(2)

                return True

            except Exception:

                continue

        return False

    def _wait_for_details(self):

        selectors = [

            ".jobs-search__job-details",

            ".jobs-details",

            ".jobs-unified-top-card",

            ".job-details-jobs-unified-top-card",

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

        time.sleep(2)