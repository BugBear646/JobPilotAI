from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config.settings import settings
from backend.db.database import initialize_database
from backend.utils.logger import get_logger

# Register SQLAlchemy models
import backend.models

# Import API router
from backend.api.routes import router


logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """

    logger.info("=" * 60)
    logger.info(f"Starting {settings.PROJECT_NAME}")
    logger.info("=" * 60)

    try:
        initialize_database()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.exception(f"Database initialization failed: {e}")
        raise

    logger.info("Application startup complete.")

    yield

    logger.info("Shutting down application.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-powered Job Application Assistant",
    version=settings.VERSION,
    lifespan=lifespan,
)

# Register routers
app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """
    Root endpoint.
    """
    return JSONResponse(
        content={
            "success": True,
            "project": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "message": "🚀 JobPilotAI Backend Running",
        }
    )


@app.get("/health", tags=["Health"])
def health():
    """
    Health check endpoint.
    """
    return JSONResponse(
        content={
            "status": "healthy",
            "project": settings.PROJECT_NAME,
        }
    )


@app.get("/info", tags=["Info"])
def info():
    """
    Application information.
    """
    return JSONResponse(
        content={
            "project": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "database": str(settings.DATABASE_PATH),
            "debug": settings.DEBUG,
            "max_applications": settings.MAX_APPLICATIONS,
        }
    )