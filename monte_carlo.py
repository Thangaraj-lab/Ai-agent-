# engine/simulation/monte_carlo.py

import numpy as np
from typing import List, Tuple

from utils.logger import get_logger
from app.config import settings


logger = get_logger(__name__)


class MonteCarloSimulator:
    """
    Performs Monte Carlo simulations to estimate
    possible future outcomes of revenue.
    """

    def __init__(self):
        self.simulations = settings.SIMULATIONS
        self.risk_factor = settings.RISK_FACTOR

    # -------------------------------
    # 🔹 MAIN METHOD
    # -------------------------------
    def run(self, values: List[float]) -> Tuple[List[np.ndarray], List[dict]]:
        logger.info("Starting Monte Carlo simulation...")

        simulations = []
        summaries = []

        for value in values:
            sim = self._simulate(value)
            simulations.append(sim)

            summary = self._summarize(sim)
            summaries.append(summary)

        logger.info("Monte Carlo simulation completed")
        return simulations, summaries

    # -------------------------------
    # 🔹 CORE SIMULATION LOGIC
    # -------------------------------
    def _simulate(self, value: float) -> np.ndarray:
        """
        Generate random distribution around value.
        """

        # standard deviation based on risk
        std_dev = max(value * self.risk_factor, 1e-6)

        # normal distribution
        simulation = np.random.normal(
            loc=value,
            scale=std_dev,
            size=self.simulations
        )

        return simulation

    # -------------------------------
    # 🔹 SUMMARY STATISTICS
    # -------------------------------
    def _summarize(self, sim: np.ndarray) -> dict:
        return {
            "mean": float(np.mean(sim)),
            "min": float(np.min(sim)),
            "max": float(np.max(sim)),
            "std": float(np.std(sim)),
        }