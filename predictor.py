# engine/prediction/predictor.py

from typing import List
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from utils.logger import get_logger


logger = get_logger(__name__)


class Predictor:
    """
    Prediction engine using ML models.
    Default: simple regression (can upgrade to XGBoost).
    """

    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.is_trained = False

    # -------------------------------
    # 🔹 TRAIN MODEL
    # -------------------------------
    def train(self, X: List[List[float]], y: List[float]):
        """
        Train model with input features.
        """

        logger.info("Training prediction model...")

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)

        self.is_trained = True

        logger.info("Model training completed")

    # -------------------------------
    # 🔹 PREDICT
    # -------------------------------
    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Predict future values.
        """

        if not self.is_trained:
            raise RuntimeError("Model not trained")

        X_scaled = self.scaler.transform(X)
        predictions = self.model.predict(X_scaled)

        return predictions.tolist()

    # -------------------------------
    # 🔹 SIMPLE AUTO TRAIN (MVP)
    # -------------------------------
    def fit_and_predict(self, values: List[float]) -> List[float]:
        """
        Quick training using index as feature.
        """

        logger.info("Running quick prediction...")

        X = np.arange(len(values)).reshape(-1, 1)
        y = np.array(values)

        self.train(X, y)
        preds = self.predict(X)

        return preds