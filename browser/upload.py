from backend.utils.logger import get_logger

logger = get_logger()


class ResumeUploader:
    """
    Handles resume upload during Easy Apply.
    If a resume is already selected, it does nothing.
    """

    def __init__(self, page, resume_path=None):
        self.page = page
        self.resume_path = resume_path

    def resume_already_selected(self):
        selectors = [
            "text=Resume",
            "text=Uploaded resume",
            "text=Recent resume",
            "span:has-text('Resume')",
        ]

        for selector in selectors:
            try:
                if self.page.locator(selector).count() > 0:
                    return True
            except Exception:
                pass

        return False

    def upload(self):
        if self.resume_already_selected():
            logger.info("Resume already selected.")
            return True

        if self.resume_path is None:
            logger.info("No resume path provided.")
            return False

        file_inputs = self.page.locator("input[type='file']")

        if file_inputs.count() == 0:
            logger.info("No upload input found.")
            return False

        try:
            logger.info("Uploading resume...")

            file_inputs.first.set_input_files(
                self.resume_path
            )

            self.page.wait_for_timeout(3000)

            logger.info("Resume uploaded.")

            return True

        except Exception as e:
            logger.info(f"Resume upload failed: {e}")
            return False