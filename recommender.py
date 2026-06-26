# engine/decision/recommender.py

from typing import List, Dict

from utils.logger import get_logger
from engine.decision.ranking import RankingEngine
from app.constants import DEFAULT_TOP_K


logger = get_logger(__name__)


class Recommender:
    """
    Generates final recommendations based on scoring logic.
    Combines performance + risk into a single decision score.
    """

    def __init__(self):
        self.ranker = RankingEngine(key="score", reverse=True)

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def recommend(self, users: List[Dict], top_k: int = DEFAULT_TOP_K) -> List[Dict]:
        """
        Returns top K recommended users.
        """

        logger.info("Generating recommendations...")

        scored_users = self._apply_scoring(users)
        ranked_users = self.ranker.rank(scored_users)
        top_users = ranked_users[:top_k]

        logger.info("Recommendation completed")
        return top_users

    # -------------------------------
    # 🔹 SCORING LOGIC
    # -------------------------------
    def _apply_scoring(self, users: List[Dict]) -> List[Dict]:
        """
        Compute score for each user.
        Score = return - risk penalty
        """

        for user in users:
            score = self._calculate_score(user)
            user["score"] = score

        return users

    # -------------------------------
    # 🔹 SCORE FORMULA
    # -------------------------------
    def _calculate_score(self, user: Dict) -> float:
        """
        Custom scoring formula.
        Can be upgraded to ML later.
        """

        mean = user.get("mean", 0)
        risk = user.get("std", 0) or user.get("risk", 0)

        # risk penalty weight
        risk_weight = 0.6

        score = mean - (risk * risk_weight)

        return float(score)

    # -------------------------------
    # 🔹 FULL PIPELINE SUPPORT
    # -------------------------------
    def recommend_with_details(self, users: List[Dict], top_k: int = DEFAULT_TOP_K) -> Dict:
        """
        Returns full ranking + top users.
        """

        scored = self._apply_scoring(users)
        ranked = self.ranker.rank(scored)
        top = ranked[:top_k]

        return {
            "all_users": ranked,
            "top_users": top
        }