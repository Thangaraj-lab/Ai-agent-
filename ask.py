# api/routes/ask.py

from fastapi import APIRouter, HTTPException
from typing import Dict

from utils.logger import get_logger
from app.constants import ErrorMessages

from schemas.request import AdvisorRequest
from schemas.response import AdvisorResponse

from services.advisor_service import AdvisorService


logger = get_logger(__name__)

router = APIRouter()
advisor_service = AdvisorService()


# -------------------------------
# 🔹 MAIN ANALYSIS ENDPOINT
# -------------------------------
@router.post(
    "/",
    response_model=AdvisorResponse,
    tags=["Advisor"]
)
def analyze(request: AdvisorRequest) -> Dict:
    """
    Main endpoint to analyze user data.
    """

    logger.info("Received analysis request")

    try:
        # Convert Pydantic → dict
        input_data = [user.dict() for user in request.users]

        # Call service
        result = advisor_service.analyze(input_data)

        return result

    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        logger.error(f"Internal error: {str(e)}")
        raise HTTPException(status_code=500, detail=ErrorMessages.INTERNAL_ERROR)