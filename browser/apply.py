from browser.browser import BrowserManager
from browser.login import login
from browser.search import LinkedInSearch


class JobApplyAgent:

    def __init__(self, config):

        self.config = config

        self.browser = None
        self.page = None

        self.search_engine = None

        self.jobs = []

    def start_browser(self):

        print("\nLaunching browser...\n")

        self.browser = BrowserManager()

        self.page = self.browser.start()

        self.search_engine = LinkedInSearch(self.page)

    def login(self):

        print("Waiting for LinkedIn login...\n")

        login(self.page)

        print("\nLogin successful.\n")

    def search(self):

        print("Opening search...\n")

        if self.config["mode"] == "url":

            self.search_engine.open_url(
                self.config["search_url"]
            )

        else:

            self.search_engine.search(
                keyword=self.config["role"],
                location=self.config["location"],
            )

    def collect_jobs(self):

        print("\nCollecting jobs...\n")

        from browser.collector import JobCollector
        collector = JobCollector(self.page)
        
        self.jobs = collector.collect(
            max_jobs=self.config["max_applications"]
        )

        print(
            f"\nCollected {len(self.jobs)} jobs.\n"
        )

    def apply(self):

        print("\nStarting applications...\n")

        applied = 0

        for job in self.jobs:

            if applied >= self.config["max_applications"]:
                break

            print("--------------------------------")
            print(job)
            print("--------------------------------")

            #
            # browser/apply_job.py
            #

            applied += 1

        print(
            f"\nApplications attempted : {applied}\n"
        )

    def summary(self):

        print("\n================================")
        print("Automation Complete")
        print("================================\n")

    def shutdown(self):

        if self.browser:

            self.browser.stop()

    def run(self):

        try:

            self.start_browser()

            self.login()

            self.search()

            self.collect_jobs()

            self.apply()

            self.summary()

        finally:

            self.shutdown()