from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from backend.db.database import Base


class Job(Base):
    """
    Represents a discovered job.

    Every job found by the browser automation
    will have exactly one row in this table.
    """

    __tablename__ = "jobs"

    # -------------------------
    # Primary Key
    # -------------------------

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    # -------------------------
    # Job Details
    # -------------------------

    company = Column(
        String(255),
        nullable=False,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    location = Column(
        String(255),
        nullable=True,
    )

    url = Column(
        Text,
        nullable=False,
        unique=True,
    )

    description = Column(
        Text,
        nullable=True,
    )

    platform = Column(
        String(50),
        default="LinkedIn",
    )

    employment_type = Column(
        String(100),
        nullable=True,
    )

    work_mode = Column(
        String(100),
        nullable=True,
    )

    # -------------------------
    # AI
    # -------------------------

    match_score = Column(
        Float,
        default=0.0,
    )

    resume_used = Column(
        String(255),
        nullable=True,
    )

    # -------------------------
    # Status
    # -------------------------

    status = Column(
        String(50),
        default="PENDING",
    )

    # -------------------------
    # Audit
    # -------------------------

    created_at = Column(
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
            f"<Job("
            f"id={self.id}, "
            f"company='{self.company}', "
            f"title='{self.title}'"
            f")>"
        )