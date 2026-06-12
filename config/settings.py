from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = "JobPilotAI"

    HEADLESS = False

    DEFAULT_LOCATION = "India"

    MAX_APPLICATIONS_PER_RUN = 50

    LINKEDIN_URL = "https://www.linkedin.com"

    JOB_SEARCH_URL = "https://www.linkedin.com/jobs/search/"

    BROWSER_PROFILE = "storage/browser_profile"


settings = Settings()