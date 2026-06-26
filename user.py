# schemas/user.py

from pydantic import BaseModel


class User(BaseModel):
    """
    Internal user schema.
    """

    user_id: str
    expected_revenue: float