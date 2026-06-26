# engine/simulation/scenarios.py

from typing import List, Dict

from utils.logger import get_logger
from app.constants import ScenarioType


logger = get_logger(__name__)


class ScenarioAnalyzer:
    """
    Generates different scenarios (base, bull, bear)
    to analyze how outcomes change under conditions.
    """

    def __init__(self, bull_factor: float = 1.2, bear_factor: float = 0.8):
        self.bull_factor = bull_factor
        self.bear_factor = bear_factor

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def generate(self, values: List[float]) -> Dict[str, List[float]]:
        logger.info("Generating scenario analysis...")

        scenarios = {
            ScenarioType.BASE.value: self._base(values),
            ScenarioType.BULL.value: self._bull(values),
            ScenarioType.BEAR.value: self._bear(values),
        }

        logger.info("Scenario generation completed")
        return scenarios

    # -------------------------------
    # 🔹 BASE SCENARIO
    # -------------------------------
    def _base(self, values: List[float]) -> List[float]:
        return values

    # -------------------------------
    # 🔹 BULL SCENARIO
    # -------------------------------
    def _bull(self, values: List[float]) -> List[float]:
        """
        Positive growth scenario
        """
        return [v * self.bull_factor for v in values]

    # -------------------------------
    # 🔹 BEAR SCENARIO
    # -------------------------------
    def _bear(self, values: List[float]) -> List[float]:
        """
        Negative / risk scenario
        """
        return [v * self.bear_factor for v in values]