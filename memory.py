# agent/memory.py

from typing import List, Dict, Any
from collections import deque
from datetime import datetime

from utils.logger import get_logger
from app.config import settings


logger = get_logger(__name__)


class Memory:
    """
    Lightweight in-memory conversation store.
    Can be extended to Redis / DB in future.
    """

    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.store: Dict[str, deque] = {}

    # -------------------------------
    # 🔹 ADD MESSAGE
    # -------------------------------
    def add(self, session_id: str, query: str, response: str):
        """
        Store query-response pair.
        """

        if not settings.ENABLE_MEMORY:
            return

        logger.debug(f"Storing memory for session: {session_id}")

        if session_id not in self.store:
            self.store[session_id] = deque(maxlen=self.max_history)

        self.store[session_id].append({
            "query": query,
            "response": response,
            "timestamp": datetime.utcnow().isoformat()
        })

    # -------------------------------
    # 🔹 GET HISTORY
    # -------------------------------
    def get(self, session_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve conversation history.
        """

        if not settings.ENABLE_MEMORY:
            return []

        return list(self.store.get(session_id, []))

    # -------------------------------
    # 🔹 CLEAR MEMORY
    # -------------------------------
    def clear(self, session_id: str):
        """
        Clear session memory.
        """

        if session_id in self.store:
            del self.store[session_id]
            logger.info(f"Memory cleared for session: {session_id}")

    # -------------------------------
    # 🔹 GET LAST MESSAGE
    # -------------------------------
    def get_last(self, session_id: str) -> Dict[str, Any]:
        """
        Get last interaction.
        """

        history = self.store.get(session_id)

        if not history:
            return {}

        return history[-1]