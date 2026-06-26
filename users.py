# api/routes/users.py

from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict

from utils.logger import get_logger
from app.constants import ErrorMessages

from services.user_service import UserService
from schemas.user import User


logger = get_logger(__name__)

router = APIRouter()
user_service = UserService()


# -------------------------------
# 🔹 ENRICH USERS
# -------------------------------
@router.post("/enrich", tags=["Users"])
def enrich_users(users: List[User]) -> List[Dict]:
    """
    Add derived metrics like ROI and efficiency.
    """

    logger.info("Enrich users request received")

    try:
        user_dicts = [u.dict() for u in users]
        enriched = user_service.enrich_users(user_dicts)

        return enriched

    except Exception as e:
        logger.error(f"Error enriching users: {str(e)}")
        raise HTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR)


# -------------------------------
# 🔹 FILTER USERS
# -------------------------------
@router.post("/filter", tags=["Users"])
def filter_users(
    users: List[User],
    min_score: float = Query(0, description="Minimum score threshold")
) -> List[Dict]:
    """
    Filter users based on score threshold.
    """

    logger.info("Filter users request received")

    try:
        user_dicts = [u.dict() for u in users]
        filtered = user_service.filter_users(user_dicts, min_score)

        return filtered

    except Exception as e:
        logger.error(f"Error filtering users: {str(e)}")
        raise HTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR)