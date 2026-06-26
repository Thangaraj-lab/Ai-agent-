# engine/explainability/explainer.py

from typing import List, Dict

from utils.logger import get_logger
from utils.helpers import round_float


logger = get_logger(__name__)


class Explainer:
    """
    Generates human-readable explanations
    for decisions and rankings.
    """

    # -------------------------------
    # 🔹 SINGLE USER EXPLANATION
    # -------------------------------
    def explain_user(self, user: Dict) -> str:
        """
        Explain why a user was selected.
        """

        user_id = user.get("user_id")
        mean = round_float(user.get("mean", 0))
        risk = round_float(user.get("risk", 0))
        score = round_float(user.get("score", 0))

        explanation = (
            f"User {user_id} shows strong expected performance "
            f"with an average return of {mean}. "
            f"The associated risk is {risk}, resulting in a final score of {score}. "
            f"This makes the user a favorable candidate."
        )

        return explanation

    # -------------------------------
    # 🔹 TOP USERS SUMMARY
    # -------------------------------
    def explain_top_users(self, users: List[Dict]) -> List[Dict]:
        """
        Attach explanation to each top user.
        """

        logger.info("Generating explanations for top users")

        return [
            {
                **user,
                "explanation": self.explain_user(user)
            }
            for user in users
        ]

    # -------------------------------
    # 🔹 GLOBAL SUMMARY
    # -------------------------------
    def explain_summary(self, users: List[Dict]) -> str:
        """
        Generate overall system-level explanation.
        """

        if not users:
            return "No users available for analysis."

        best = users[0]

        summary = (
            f"The analysis evaluated {len(users)} users. "
            f"User {best['user_id']} stands out as the best candidate "
            f"based on highest score and balanced risk-return profile."
        )

        return summary