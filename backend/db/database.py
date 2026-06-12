from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from backend.utils.logger import get_logger

logger = get_logger()

# ---------------------------------------------------
# Ensure database directory exists
# ---------------------------------------------------

Path(settings.DATABASE_DIR).mkdir(
    parents=True,
    exist_ok=True,
)

# ---------------------------------------------------
# SQLite Database
# ---------------------------------------------------

DATABASE_URL = f"sqlite:///{settings.DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency.

    Example:

        db = next(get_db())
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def initialize_database():
    """
    Creates all tables.

    This should be called once during application startup.
    """

    logger.info("Initializing database...")

    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized successfully.")