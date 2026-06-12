from backend.utils.logger import get_logger

logger = get_logger()


class FormFiller:
    """
    Generic LinkedIn Easy Apply form filler.

    Currently supports:
    - Text inputs
    - Textareas
    - Select dropdowns

    Future:
    - Radio buttons
    - Checkboxes
    - Date pickers
    - Uploads
    """

    def __init__(self, page, profile):
        self.page = page
        self.profile = profile

    def get_answer(self, label: str):

        label = label.lower()

        mappings = {
            "phone": self.profile.get("phone", ""),
            "mobile": self.profile.get("phone", ""),
            "email": self.profile.get("email", ""),
            "city": self.profile.get("city", ""),
            "location": self.profile.get("city", ""),
            "notice": self.profile.get("notice_period", ""),
            "current ctc": self.profile.get("current_ctc", ""),
            "expected": self.profile.get("expected_ctc", ""),
            "salary": self.profile.get("expected_ctc", ""),
            "linkedin": self.profile.get("linkedin", ""),
            "github": self.profile.get("github", ""),
            "portfolio": self.profile.get("portfolio", ""),
        }

        for key, value in mappings.items():
            if key in label:
                return str(value)

        return ""

    def fill_text_inputs(self):

        inputs = self.page.locator(
            "input[type='text'], input:not([type])"
        )

        count = inputs.count()

        logger.info(f"Found {count} text inputs")

        for i in range(count):

            try:

                input_box = inputs.nth(i)

                if not input_box.is_visible():
                    continue

                label = ""

                try:
                    label = input_box.get_attribute(
                        "aria-label"
                    ) or ""
                except Exception:
                    pass

                answer = self.get_answer(label)

                if answer == "":
                    continue

                input_box.fill(answer)

                logger.info(
                    f"Filled '{label}' -> '{answer}'"
                )

            except Exception:
                pass

    def fill_textareas(self):

        textareas = self.page.locator("textarea")

        count = textareas.count()

        logger.info(f"Found {count} textareas")

        for i in range(count):

            try:

                textarea = textareas.nth(i)

                if not textarea.is_visible():
                    continue

                label = textarea.get_attribute(
                    "aria-label"
                ) or ""

                answer = self.get_answer(label)

                if answer == "":
                    continue

                textarea.fill(answer)

                logger.info(
                    f"Filled textarea '{label}'"
                )

            except Exception:
                pass

    def fill_dropdowns(self):

        selects = self.page.locator("select")

        count = selects.count()

        logger.info(f"Found {count} dropdowns")

        for i in range(count):

            try:

                select = selects.nth(i)

                if not select.is_visible():
                    continue

                label = select.get_attribute(
                    "aria-label"
                ) or ""

                answer = self.get_answer(label)

                if answer == "":
                    continue

                try:
                    select.select_option(label=answer)
                except Exception:
                    try:
                        select.select_option(value=answer)
                    except Exception:
                        pass

                logger.info(
                    f"Selected dropdown '{label}'"
                )

            except Exception:
                pass

    def fill(self):

        logger.info(
            "Starting form filling..."
        )

        self.fill_text_inputs()

        self.fill_textareas()

        self.fill_dropdowns()

        logger.info(
            "Form filling completed."
        )