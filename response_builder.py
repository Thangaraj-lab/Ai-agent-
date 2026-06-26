# agent/response_builder.py

from typing import Dict, Any

from utils.logger import get_logger


logger = get_logger(__name__)


class ResponseBuilder:
    """
    Formats and structures final responses from the agent.
    Ensures consistency for API/UI consumption.
    """

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def build(self, raw_response: str, intent: str) -> Dict[str, Any]:
        """
        Convert raw LLM output into structured format.
        """

        logger.info("Building final response...")

        return {
            "intent": intent,
            "message": self._clean_response(raw_response),
            "metadata": self._build_metadata(raw_response)
        }

    # -------------------------------
    # 🔹 CLEAN RESPONSE
    # -------------------------------
    def _clean_response(self, text: str) -> str:
        """
        Clean and normalize text output.
        """

        if not text:
            return "No response generated."

        # basic cleanup
        cleaned = text.strip()

        return cleaned

    # -------------------------------
    # 🔹 METADATA BUILDER
    # -------------------------------
    def _build_metadata(self, text: str) -> Dict[str, Any]:
        """
        Attach useful metadata (length, tokens, etc.)
        """

        return {
            "length": len(text),
            "word_count": len(text.split())
        }