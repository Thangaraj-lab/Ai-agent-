# api/routes/health.py

from fastapi import APIRouter
from datetime import datetime

from utils.logger import get_logger
from app.config import settings


logger = get_logger(__name__)

router = APIRouter()


@router.get("/", tags=["Health"])
def health_check():
    """
    Basic health check endpoint.
    """

    logger.info("Health check requested")

    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "environment": settings.ENV,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/detailed", tags=["Health"])
def detailed_health():
    """
    Extended health check (can include DB, cache later).
    """

    logger.info("Detailed health check requested")

    return {
        "status": "healthy",
        "services": {
            "api": "up",
            "engine": "up",
            "agent": "up"
        },
        "timestamp": datetime.utcnow().isoformat()
    }