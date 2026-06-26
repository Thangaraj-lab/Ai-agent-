# services/company_service.py

from typing import Dict, List
from utils.logger import get_logger


logger = get_logger(__name__)


class CompanyService:
    """
    Handles company-level operations and aggregations.
    """

    def summarize(self, users: List[Dict]) -> Dict:
        """
        Generate company-level summary metrics.
        """

        logger.info("Generating company summary...")

        if not users:
            return {
                "total_users": 0,
                "avg_revenue": 0,
                "avg_risk": 0
            }

        total_users = len(users)
        total_revenue = sum(u.get("mean", 0) for u in users)
        total_risk = sum(u.get("risk", 0) for u in users)

        return {
            "total_users": total_users,
            "avg_revenue": total_revenue / total_users,
            "avg_risk": total_risk / total_users
        }

    def get_top_performers(self, users: List[Dict], threshold: float) -> List[Dict]:
        """
        Filter high-performing users.
        """

        return [
            u for u in users
            if u.get("mean", 0) >= threshold
        ]