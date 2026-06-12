from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from backend.db.database import Base


class Application(Base):
    """
    Stores one application attempt for a job.

    One Job can have multiple application attempts
    in the future if needed.
    """

    __tablename__ = "applications"

    # ------------------------
    # Primary Key
    # ------------------------

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    # ------------------------
    # Foreign Key
    # ------------------------

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
    )

    # ------------------------
    # Status
    # ------------------------

    status = Column(
        String(50),
        default="PENDING",
    )

    # ------------------------
    # Resume Used
    # ------------------------

    resume_used = Column(
        String(255),
        nullable=True,
    )

    # ------------------------
    # AI Generated Answer Summary
    # ------------------------

    answer_summary = Column(
        Text,
        nullable=True,
    )

    # ------------------------
    # Failure Reason
    # ------------------------

    failure_reason = Column(
        Text,
        nullable=True,
    )

    # ------------------------
    # Tracking
    # ------------------------

    applied_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    def __repr__(self):

        return (
            f"<Application("
            f"id={self.id}, "
            f"job_id={self.job_id}, "
            f"status='{self.status}'"
            f")>"
        )