from enum import Enum


class ApplicationStatus(str, Enum):
    PENDING = "PENDING"
    REVIEW = "REVIEW"
    APPLIED = "APPLIED"
    SKIPPED = "SKIPPED"
    FAILED = "FAILED"


class JobPlatform(str, Enum):
    LINKEDIN = "LINKEDIN"


class BrowserType(str, Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


class EmploymentType(str, Enum):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    CONTRACT = "Contract"
    INTERN = "Internship"
    TEMPORARY = "Temporary"
    UNKNOWN = "Unknown"


class WorkMode(str, Enum):
    REMOTE = "Remote"
    HYBRID = "Hybrid"
    ONSITE = "Onsite"
    UNKNOWN = "Unknown"


class ExperienceLevel(str, Enum):
    INTERN = "Intern"
    ENTRY = "Entry"
    ASSOCIATE = "Associate"
    MID = "Mid"
    SENIOR = "Senior"
    LEAD = "Lead"
    DIRECTOR = "Director"
    UNKNOWN = "Unknown"


SUPPORTED_RESUME_EXTENSIONS = [
    ".pdf"
]


MAX_APPLICATIONS_PER_RUN = 200

DEFAULT_TIMEOUT_MS = 30000

DEFAULT_WAIT_MS = 1500

DEFAULT_SCREENSHOT_NAME = "debug.png"

DEFAULT_DATABASE_NAME = "jobpilot.db"

PROJECT_NAME = "JobPilotAI"

VERSION = "0.1.0"