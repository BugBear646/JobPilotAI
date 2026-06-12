from sqlalchemy.orm import Session

from backend.models.job import Job
from backend.schemas.job import JobCreate


def create_job(
    db: Session,
    job: JobCreate,
) -> Job:
    """
    Create a new job.
    """

    db_job = Job(
        company=job.company,
        title=job.title,
        url=job.url,
        location=job.location,
        description=job.description,
        platform=job.platform,
        employment_type=job.employment_type,
        work_mode=job.work_mode,
    )

    db.add(db_job)

    db.commit()

    db.refresh(db_job)

    return db_job


def get_jobs(
    db: Session,
):
    """
    Return all jobs.
    """

    return (
        db.query(Job)
        .order_by(Job.id.desc())
        .all()
    )


def get_job(
    db: Session,
    job_id: int,
):
    return (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )


def delete_job(
    db: Session,
    job_id: int,
):
    job = (
        db.query(Job)
        .filter(Job.id == job_id)
        .first()
    )

    if job:

        db.delete(job)

        db.commit()

    return job