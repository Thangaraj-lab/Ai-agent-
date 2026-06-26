# engine/simulation/risk.py

import numpy as np
from typing import List

from utils.logger import get_logger
from app.constants import DEFAULT_CONFIDENCE_LEVEL


logger = get_logger(__name__)


class RiskAnalyzer:
    """
    Calculates risk metrics from simulation results.
    Includes VaR, volatility, and downside risk.
    """

    def __init__(self, confidence: float = DEFAULT_CONFIDENCE_LEVEL):
        self.confidence = confidence

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def calculate(self, simulations: List[np.ndarray]) -> List[dict]:
        logger.info("Starting risk analysis...")

        results = []

        for sim in simulations:
            result = self._analyze_single(sim)
            results.append(result)

        logger.info("Risk analysis completed")
        return results

    # -------------------------------
    # 🔹 SINGLE SIM ANALYSIS
    # -------------------------------
    def _analyze_single(self, sim: np.ndarray) -> dict:
        mean = np.mean(sim)

        return {
            "var": self._calculate_var(sim),
            "std": float(np.std(sim)),
            "downside_risk": self._downside_risk(sim, mean),
        }

    # -------------------------------
    # 🔹 VALUE AT RISK (VaR)
    # -------------------------------
    def _calculate_var(self, sim: np.ndarray) -> float:
        """
        VaR at given confidence level.
        Example: 95% VaR → worst 5% outcome
        """

        percentile = (1 - self.confidence) * 100
        return float(np.percentile(sim, percentile))

    # -------------------------------
    # 🔹 DOWNSIDE RISK
    # -------------------------------
    def _downside_risk(self, sim: np.ndarray, mean: float) -> float:
        """
        Measures average of values below mean.
        """

        downside = sim[sim < mean]

        if len(downside) == 0:
            return 0.0

        return float(np.mean(downside))