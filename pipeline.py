# engine/pipeline.py

from typing import List, Dict

from utils.logger import get_logger

from engine.data.loader import DataLoader
from engine.data.validator import DataValidator

from engine.simulation.monte_carlo import MonteCarloSimulator
from engine.simulation.risk import RiskAnalyzer
from engine.simulation.scenarios import ScenarioAnalyzer

from engine.decision.classifier import Classifier
from engine.decision.recommender import Recommender

from engine.explainability.explainer import Explainer


logger = get_logger(__name__)


class Pipeline:
    """
    Core orchestration layer.
    Connects all components into a full decision system.
    """

    def __init__(self):
        # Data layer
        self.loader = DataLoader()
        self.validator = DataValidator()

        # Simulation layer
        self.simulator = MonteCarloSimulator()
        self.risk_analyzer = RiskAnalyzer()
        self.scenario_analyzer = ScenarioAnalyzer()

        # Decision layer
        self.classifier = Classifier()
        self.recommender = Recommender()

        # Explainability
        self.explainer = Explainer()

    # -------------------------------
    # 🔹 MAIN PIPELINE EXECUTION
    # -------------------------------
    def run(self, source) -> Dict:
        logger.info("Pipeline started")

        # 1️⃣ Load data
        df = self.loader.load(source)

        # 2️⃣ Validate data
        df = self.validator.validate(df)

        # 3️⃣ Extract values
        values = df["expected_revenue"].tolist()

        # 4️⃣ Scenario analysis (optional)
        scenarios = self.scenario_analyzer.generate(values)

        # 5️⃣ Simulation (use base scenario)
        simulations, summaries = self.simulator.run(scenarios["base"])

        # 6️⃣ Risk calculation
        risks = self.risk_analyzer.calculate(simulations)

        # 7️⃣ Merge all data
        users = self._merge_results(df, summaries, risks)

        # 8️⃣ Classification
        users = self.classifier.classify_batch(users)

        # 9️⃣ Recommendation
        result = self.recommender.recommend_with_details(users)

        # 🔟 Explainability
        result["top_users"] = self.explainer.explain_top_users(result["top_users"])
        result["summary"] = self.explainer.explain_summary(result["top_users"])

        logger.info("Pipeline completed")

        return result

    # -------------------------------
    # 🔹 MERGE RESULTS
    # -------------------------------
    def _merge_results(
        self,
        df,
        summaries: List[Dict],
        risks: List[Dict]
    ) -> List[Dict]:
        """
        Combine simulation + risk + raw data
        """

        users = []

        for i, row in df.iterrows():
            user = {
                "user_id": row["user_id"],
                "expected_revenue": row["expected_revenue"],
                "mean": summaries[i]["mean"],
                "min": summaries[i]["min"],
                "max": summaries[i]["max"],
                "std": summaries[i]["std"],
                "risk": risks[i]["std"],
                "var": risks[i]["var"],
            }

            users.append(user)

        return users