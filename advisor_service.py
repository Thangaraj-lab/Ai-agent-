# services/advisor_service.py

from typing import List, Dict, Any

from utils.logger import get_logger
from utils.formatters import format_response, build_decision_summary

from engine.pipeline import Pipeline
from engine.optimization.solver import OptimizationSolver
from engine.prediction.predictor import Predictor


logger = get_logger(__name__)


class AdvisorService:
    """
    Service layer that coordinates pipeline,
    prediction, optimization, and formatting.
    """

    def __init__(self):
        self.pipeline = Pipeline()
        self.optimizer = OptimizationSolver()
        self.predictor = Predictor()

    # -------------------------------
    # 🔹 MAIN ENTRY (API CALL)
    # -------------------------------
    def analyze(self, source: Any) -> Dict:
        """
        Full analysis pipeline.
        """

        logger.info("Advisor service started")

        # 1️⃣ Run core pipeline
        result = self.pipeline.run(source)

        all_users = result.get("all_users", [])
        top_users = result.get("top_users", [])

        # 2️⃣ Prediction (optional enhancement)
        predictions = self._run_prediction(all_users)

        # 3️⃣ Optimization (optional enhancement)
        optimized_users = self._run_optimization(all_users)

        # 4️⃣ Final formatting
        formatted = format_response(all_users, top_users)

        # 5️⃣ Add extra insights
        formatted["decision_summary"] = build_decision_summary(top_users)
        formatted["predictions"] = predictions
        formatted["optimized_selection"] = optimized_users

        logger.info("Advisor service completed")

        return formatted

    # -------------------------------
    # 🔹 PREDICTION LAYER
    # -------------------------------
    def _run_prediction(self, users: List[Dict]) -> List[float]:
        """
        Predict trends based on historical-like data.
        """

        if not users:
            return []

        values = [u.get("mean", 0) for u in users]

        try:
            predictions = self.predictor.fit_and_predict(values)
            return predictions

        except Exception as e:
            logger.warning(f"Prediction failed: {str(e)}")
            return []

    # -------------------------------
    # 🔹 OPTIMIZATION LAYER
    # -------------------------------
    def _run_optimization(self, users: List[Dict]) -> List[Dict]:
        """
        Optimize selection using constraints.
        """

        if not users:
            return []

        try:
            optimized = self.optimizer.solve(users, budget=None)
            return optimized

        except Exception as e:
            logger.warning(f"Optimization failed: {str(e)}")
            return []