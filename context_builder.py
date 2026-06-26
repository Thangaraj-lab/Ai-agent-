# agent/context_builder.py

from typing import Dict, Any

from utils.logger import get_logger


logger = get_logger(__name__)


class ContextBuilder:
    """
    Builds contextual information for the agent
    based on query, intent, and system data.
    """

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def build(self, query: str, data: Dict = None, intent: str = "general") -> Dict[str, Any]:
        """
        Create structured context for prompt generation.
        """

        logger.info("Building context for agent...")

        context = {
            "query": query,
            "intent": intent,
            "data_summary": self._summarize_data(data),
            "key_insights": self._extract_insights(data, intent)
        }

        return context

    # -------------------------------
    # 🔹 DATA SUMMARY
    # -------------------------------
    def _summarize_data(self, data: Dict) -> Dict:
        """
        Extract high-level summary from system output.
        """

        if not data:
            return {}

        users = data.get("all_users", [])

        return {
            "total_users": len(users),
            "top_user": users[0]["user_id"] if users else None
        }

    # -------------------------------
    # 🔹 INSIGHTS EXTRACTION
    # -------------------------------
    def _extract_insights(self, data: Dict, intent: str) -> Dict:
        """
        Extract relevant insights based on intent.
        """

        if not data:
            return {}

        users = data.get("all_users", [])

        if intent == "top_users":
            return {
                "top_users": [u["user_id"] for u in data.get("top_users", [])]
            }

        elif intent == "risk_analysis":
            return {
                "high_risk_users": [
                    u["user_id"]
                    for u in users
                    if u.get("risk", 0) > 100
                ]
            }

        elif intent == "performance":
            return {
                "high_performance_users": [
                    u["user_id"]
                    for u in users
                    if u.get("mean", 0) > 1500
                ]
            }

        elif intent == "summary":
            return {
                "summary": data.get("summary", "")
            }

        return {}