from fastapi import FastAPI
from contextlib import asynccontextmanager

from config.settings import settings
from backend.db.database import initialize_database
from backend.utils.logger import get_logger

# Import all models so SQLAlchemy registers them
import backend.models

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup Events
    """

    logger.info("=" * 60)
    logger.info(f"Starting {settings.PROJECT_NAME}")
    logger.info("=" * 60)

    initialize_database()

    logger.info("Application started successfully.")

    yield

    logger.info("Application shutting down.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {
        "success": True,
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "message": "JobPilotAI Backend Running 🚀",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }