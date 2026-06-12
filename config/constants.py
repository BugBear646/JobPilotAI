"""
==================================================
JobPilotAI Constants
==================================================
Reusable constants used throughout the project.

Avoid hardcoding selectors or values elsewhere.
==================================================
"""

# ==============================================
# Application
# ==============================================

APP_NAME = "JobPilotAI"

VERSION = "1.0.0"

# ==============================================
# Limits
# ==============================================

MIN_APPLICATIONS = 1

DEFAULT_APPLICATIONS = 50

MAX_APPLICATIONS = 50

# ==============================================
# Timeouts (milliseconds)
# ==============================================

DEFAULT_TIMEOUT = 30000

SHORT_TIMEOUT = 5000

LONG_TIMEOUT = 60000

# ==============================================
# Sleep Durations (seconds)
# ==============================================

PAGE_LOAD_WAIT = 2

CLICK_WAIT = 1

SCROLL_WAIT = 2

MODAL_WAIT = 1

# ==============================================
# LinkedIn Selectors
# ==============================================

JOB_LIST = "div.scaffold-layout__list"

JOB_CARD = "div[data-job-id]"

JOB_TITLE = "a.job-card-list__title"

COMPANY_NAME = ".artdeco-entity-lockup__subtitle"

LOCATION = ".artdeco-entity-lockup__caption"

EASY_APPLY_BUTTON = (
    "button.jobs-apply-button"
)

NEXT_BUTTON = (
    "button[aria-label='Continue to next step']"
)

REVIEW_BUTTON = (
    "button[aria-label='Review your application']"
)

SUBMIT_BUTTON = (
    "button[aria-label='Submit application']"
)

CLOSE_BUTTON = (
    "button[aria-label='Dismiss']"
)

FOLLOW_COMPANY_CHECKBOX = (
    "input[type='checkbox']"
)

# ==============================================
# Supported Roles
# ==============================================

ROLE_SEPARATOR = ","

# ==============================================
# Browser
# ==============================================

USER_AGENT = (
    "Mozilla/5.0 "
    "(Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/137.0.0.0 "
    "Safari/537.36"
)

# ==============================================
# Status
# ==============================================

STATUS_APPLIED = "Applied"

STATUS_SKIPPED = "Skipped"

STATUS_FAILED = "Failed"

STATUS_ALREADY_APPLIED = "Already Applied"

# ==============================================
# Logging
# ==============================================

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(message)s"
)