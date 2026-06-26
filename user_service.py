# services/user_service.py

from typing import List, Dict
from utils.logger import get_logger


logger = get_logger(__name__)


class UserService:
    """
    Handles user-level operations and transformations.
    """

    def enrich_users(self, users: List[Dict]) -> List[Dict]:
        """
        Add derived metrics per user.
        """

        logger.info("Enriching user data...")

        enriched = []

        for u in users:
            enriched.append({
                **u,
                "roi": self._calculate_roi(u),
                "efficiency": self._efficiency(u)
            })

        return enriched

    def filter_users(self, users: List[Dict], min_score: float) -> List[Dict]:
        """
        Filter users by minimum score.
        """

        return [
            u for u in users
            if u.get("score", 0) >= min_score
        ]

    # -------------------------------
    # 🔹 INTERNAL METHODS
    # -------------------------------
    def _calculate_roi(self, user: Dict) -> float:
        revenue = user.get("mean", 0)
        cost = user.get("expected_revenue", 1)

        return revenue / cost if cost else 0.0

    def _efficiency(self, user: Dict) -> float:
        score = user.get("score", 0)
        risk = user.get("risk", 1)

        return score / risk if risk else 0.0