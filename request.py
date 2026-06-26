# schemas/request.py

from pydantic import BaseModel, Field
from typing import List


class UserInput(BaseModel):
    """
    Single user input schema.
    """

    user_id: str = Field(..., description="Unique user identifier")
    expected_revenue: float = Field(..., ge=0, description="Expected revenue value")


class AdvisorRequest(BaseModel):
    """
    Request schema for analysis endpoint.
    """

    users: List[UserInput]

    class Config:
        schema_extra = {
            "example": {
                "users": [
                    {"user_id": "U1", "expected_revenue": 1000},
                    {"user_id": "U2", "expected_revenue": 2000}
                ]
            }
        }