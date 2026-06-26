# engine/decision/ranking.py

from typing import List, Dict, Callable

from utils.logger import get_logger


logger = get_logger(__name__)


class RankingEngine:
    """
    Responsible for ranking users based on scoring logic.
    Supports flexible ranking strategies.
    """

    def __init__(self, key: str = "score", reverse: bool = True):
        self.key = key
        self.reverse = reverse

    # -------------------------------
    # 🔹 MAIN RANK METHOD
    # -------------------------------
    def rank(self, users: List[Dict]) -> List[Dict]:
        """
        Sort users based on configured key.
        """

        logger.info(f"Ranking users by '{self.key}'")

        ranked = sorted(
            users,
            key=lambda x: self._safe_get(x, self.key),
            reverse=self.reverse
        )

        logger.info("Ranking completed")
        return ranked

    # -------------------------------
    # 🔹 TOP-K SELECTOR
    # -------------------------------
    def top_k(self, users: List[Dict], k: int) -> List[Dict]:
        """
        Return top K ranked users.
        """

        ranked = self.rank(users)
        return ranked[:k]

    # -------------------------------
    # 🔹 CUSTOM RANKING FUNCTION
    # -------------------------------
    def rank_with(self, users: List[Dict], func: Callable) -> List[Dict]:
        """
        Rank users using custom scoring function.
        """

        logger.info("Ranking using custom function")

        ranked = sorted(
            users,
            key=func,
            reverse=self.reverse
        )

        return ranked

    # -------------------------------
    # 🔹 SAFE GET
    # -------------------------------
    def _safe_get(self, data: Dict, key: str) -> float:
        """
        Avoid key errors during sorting.
        """

        value = data.get(key)

        if value is None:
            return float("-inf") if self.reverse else float("inf")

        return value