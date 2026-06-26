# engine/decision/classifier.py

from typing import Dict

from utils.logger import get_logger
from app.constants import UserSegment


logger = get_logger(__name__)


class Classifier:
    """
    Classifies users into segments based on performance metrics.
    Used for decision-making and prioritization.
    """

    def classify(self, user: Dict) -> str:
        """
        Classify a single user based on mean performance.
        """

        mean_value = user.get("mean", 0)

        segment = self._get_segment(mean_value)

        logger.debug(f"User {user.get('user_id')} classified as {segment}")

        return segment

    # -------------------------------
    # 🔹 SEGMENT LOGIC
    # -------------------------------
    def _get_segment(self, value: float) -> str:
        """
        Define segmentation thresholds.
        Can be tuned later dynamically.
        """

        if value >= 2000:
            return UserSegment.PREMIUM.value

        elif value >= 1200:
            return UserSegment.HIGH.value

        elif value >= 600:
            return UserSegment.MEDIUM.value

        else:
            return UserSegment.LOW.value

    # -------------------------------
    # 🔹 BULK CLASSIFICATION
    # -------------------------------
    def classify_batch(self, users: list) -> list:
        """
        Apply classification to multiple users.
        """

        return [
            {
                **user,
                "segment": self.classify(user)
            }
            for user in users
        ]