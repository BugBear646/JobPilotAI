from backend.utils.logger import get_logger

from browser.collector import JobCollector
from browser.apply_job import JobApplier

logger = get_logger()


class ApplyEngine:

    def __init__(
        self,
        page,
        profile,
        resume_path=None,
        max_applications=10,
    ):
        self.page = page
        self.profile = profile
        self.resume_path = resume_path
        self.max_applications = max_applications

    def start(self):

        logger.info("")
        logger.info("=" * 80)
        logger.info("Collecting jobs...")
        logger.info("=" * 80)

        collector = JobCollector(self.page)

        jobs = collector.collect()

        logger.info(f"Collected {len(jobs)} jobs.")

        if len(jobs) == 0:
            logger.info("No jobs found.")
            return

        applier = JobApplier(
            page=self.page,
            profile=self.profile,
            resume_path=self.resume_path,
        )

        applied = 0
        skipped = 0
        failed = 0

        for index, job in enumerate(jobs):

            if applied >= self.max_applications:
                logger.info("")
                logger.info(
                    f"Reached limit of {self.max_applications} applications."
                )
                break

            logger.info("")
            logger.info("=" * 80)
            logger.info(
                f"Processing Job {index + 1}/{len(jobs)}"
            )
            logger.info("=" * 80)

            logger.info(
                f"Company : {job.get('company','')}"
            )
            logger.info(
                f"Title    : {job.get('title','')}"
            )

            try:

                success = applier.apply(job)

                if success:
                    applied += 1
                    logger.info(
                        "Status : APPLIED"
                    )
                else:
                    skipped += 1
                    logger.info(
                        "Status : SKIPPED"
                    )

            except Exception as e:

                failed += 1

                logger.exception(e)

                logger.info(
                    "Status : FAILED"
                )

        logger.info("")
        logger.info("=" * 80)
        logger.info("SUMMARY")
        logger.info("=" * 80)

        logger.info(
            f"Applied : {applied}"
        )

        logger.info(
            f"Skipped : {skipped}"
        )

        logger.info(
            f"Failed  : {failed}"
        )

        logger.info("=" * 80)