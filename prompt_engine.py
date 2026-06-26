# agent/prompt_engine.py

from typing import Dict

from utils.logger import get_logger


logger = get_logger(__name__)


class PromptEngine:
    """
    Responsible for generating structured prompts
    for the LLM based on query, intent, and context.
    """

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def create_prompt(self, query: str, context: Dict, intent: str) -> str:
        """
        Build final prompt string.
        """

        logger.info("Generating prompt for LLM...")

        system_prompt = self._get_system_prompt(intent)
        context_block = self._format_context(context)

        final_prompt = f"""
{system_prompt}

Context:
{context_block}

User Query:
{query}

Provide a clear, concise, and intelligent response.
"""

        return final_prompt.strip()

    # -------------------------------
    # 🔹 SYSTEM PROMPT (INTENT BASED)
    # -------------------------------
    def _get_system_prompt(self, intent: str) -> str:
        """
        Define behavior of AI based on intent.
        """

        prompts = {
            "top_users": "You are a business analyst. Recommend the best users based on performance.",
            "risk_analysis": "You are a risk analyst. Explain risks clearly.",
            "performance": "You are a performance analyst. Analyze returns and growth.",
            "comparison": "You are a strategic analyst. Compare options clearly.",
            "summary": "You are an executive assistant. Provide a concise summary.",
            "general": "You are an intelligent assistant helping with business decisions."
        }

        return prompts.get(intent, prompts["general"])

    # -------------------------------
    # 🔹 CONTEXT FORMATTER
    # -------------------------------
    def _format_context(self, context: Dict) -> str:
        """
        Convert context dictionary into readable text.
        """

        lines = []

        for key, value in context.items():
            lines.append(f"{key}: {value}")

        return "\n".join(lines)

