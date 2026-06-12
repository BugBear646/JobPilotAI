from time import sleep
from playwright.sync_api import Page


class JobCrawler:

    def __init__(self, page: Page):
        self.page = page
        self.visited = set()

    def load_all_jobs(self, target=50):
        """
        Scroll the LEFT jobs panel until we collect target jobs
        or LinkedIn stops loading more.
        """

        print("\nCollecting jobs...\n")

        sidebar = self.page.locator("div.scaffold-layout__list")

        previous_count = 0
        stagnant = 0

        while True:

            cards = self.page.locator(
                "li[data-occludable-job-id]"
            )

            count = cards.count()

            for i in range(count):

                try:
                    card = cards.nth(i)

                    job_id = card.get_attribute(
                        "data-occludable-job-id"
                    )

                    if job_id:
                        self.visited.add(job_id)

                except:
                    pass

            print(
                f"Collected {len(self.visited)} jobs"
            )

            if len(self.visited) >= target:
                break

            if len(self.visited) == previous_count:
                stagnant += 1
            else:
                stagnant = 0

            if stagnant >= 4:
                break

            previous_count = len(self.visited)

            sidebar.evaluate(
                "(el)=>el.scrollBy(0,1000)"
            )

            sleep(2)

        return list(self.visited)

    def visit_jobs(self):

        jobs = list(self.visited)

        print(f"\nVisiting {len(jobs)} jobs\n")

        for index, job in enumerate(jobs):

            url = f"https://www.linkedin.com/jobs/view/{job}/"

            print(url)

            self.page.goto(
                url,
                wait_until="domcontentloaded"
            )

            sleep(4)

            print(
                f"Visited {index+1}/{len(jobs)}"
            )