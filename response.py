# schemas/response.py

from pydantic import BaseModel
from typing import List, Optional


class UserResult(BaseModel):
    """
    Processed user output.
    """

    user_id: str
    mean: float
    min: Optional[float]
    max: Optional[float]
    risk: float
    score: float
    segment: Optional[str]
    explanation: Optional[str]


class Summary(BaseModel):
    total_users: int
    top_selected: int


class AdvisorResponse(BaseModel):
    """
    Final API response schema.
    """

    summary: Summary
    all_users: List[UserResult]
    top_users: List[UserResult]
    decision_summary: Optional[str]
    predictions: Optional[List[float]]
    optimized_selection: Optional[List[UserResult]]