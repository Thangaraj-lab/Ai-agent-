# schemas/company.py

from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):
    """
    Company-level schema.
    """

    name: str
    industry: Optional[str]
    total_budget: Optional[float]