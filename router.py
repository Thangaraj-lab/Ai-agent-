# agent/router.py

from typing import Dict
import re

from utils.logger import get_logger


logger = get_logger(__name__)


class AgentRouter:
    """
    Detects user intent from query.
    Routes query to appropriate logic.
    """

    def __init__(self):
        self.intent_map = self._build_intent_map()

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def detect_intent(self, query: str) -> str:
        """
        Identify user intent using rule-based matching.
        """

        query_lower = query.lower()

        for intent, patterns in self.intent_map.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    logger.info(f"Detected intent: {intent}")
                    return intent

        logger.info("Default intent: general")
        return "general"

    # -------------------------------
    # 🔹 INTENT DEFINITIONS
    # -------------------------------
    def _build_intent_map(self) -> Dict[str, list]:
        """
        Define patterns for each intent.
        """

        return {
            "top_users": [
                r"best",
                r"top",
                r"highest",
                r"recommend"
            ],

            "risk_analysis": [
                r"risk",
                r"loss",
                r"downside",
                r"danger"
            ],

            "performance": [
                r"performance",
                r"return",
                r"revenue",
                r"profit"
            ],

            "comparison": [
                r"compare",
                r"difference",
                r"vs"
            ],

            "summary": [
                r"summary",
                r"overview",
                r"report"
            ]
        }