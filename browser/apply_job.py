from backend.utils.logger import get_logger

from browser.navigator import Navigator
from browser.upload import ResumeUploader
from browser.form_filler import FormFiller

logger = get_logger()


class JobApplier:
    """
    Handles the complete Easy Apply workflow.

    Flow:

    Open Job
        ↓
    Click Easy Apply
        ↓
    Upload Resume (if needed)
        ↓
    Fill Form
        ↓
    Next
        ↓
    Fill Form
        ↓
    Review
        ↓
    Submit
        ↓
    Close Popup
    """

    def __init__(self, page, profile, resume_path=None):
        self.page = page
        self.profile = profile
        self.resume_path = resume_path

        self.navigator = Navigator(page)
        self.uploader = ResumeUploader(
            page,
            resume_path=resume_path,
        )
        self.form_filler = FormFiller(
            page,
            profile,
        )

    def open_job(self, job):

        url = job.get("url")

        if not url:
            logger.info("Job URL missing.")
            return False

        logger.info(f"Opening Job: {url}")

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000,
        )

        self.page.wait_for_timeout(3000)

        return True

    def click_easy_apply(self):

        selectors = [
            "button:has-text('Easy Apply')",
            "button.jobs-apply-button",
            "[aria-label*='Easy Apply']",
        ]

        for selector in selectors:

            try:

                button = self.page.locator(selector).first

                if button.count() == 0:
                    continue

                if button.is_visible():

                    logger.info(
                        "Easy Apply button found."
                    )

                    button.click()

                    self.page.wait_for_timeout(3000)

                    return True

            except Exception:
                pass

        logger.info(
            "Easy Apply button not found."
        )

        return False

    def close_popup(self):

        selectors = [
            "button[aria-label='Dismiss']",
            "button[aria-label='Close']",
            "button.artdeco-modal__dismiss",
        ]

        for selector in selectors:

            try:

                button = self.page.locator(selector).first

                if button.count() == 0:
                    continue

                if button.is_visible():

                    button.click()

                    self.page.wait_for_timeout(1000)

                    logger.info(
                        "Popup closed."
                    )

                    return

            except Exception:
                pass

    def apply(self, job):

        logger.info(
            "=================================="
        )
        logger.info(
            f"Applying: {job.get('company','')} | {job.get('title','')}"
        )
        logger.info(
            "=================================="
        )

        if not self.open_job(job):
            return False

        if not self.click_easy_apply():
            logger.info(
                "Skipping (No Easy Apply)."
            )
            return False

        self.uploader.upload()

        safety_counter = 0

        while safety_counter < 15:

            safety_counter += 1

            self.form_filler.fill()

            status = self.navigator.process()

            if status == "submitted":

                logger.info(
                    "Application submitted."
                )

                self.close_popup()

                return True

            if status == "stopped":

                logger.info(
                    "Workflow stopped."
                )

                self.close_popup()

                return False

        logger.info(
            "Exceeded maximum navigation steps."
        )

        self.close_popup()

        return False