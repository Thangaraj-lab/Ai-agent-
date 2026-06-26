import pandas as pd
from typing import List
from utils.logger import get_logger
from app.constants import ErrorMessages

# engine/data/validator.py




logger = get_logger(__name__)


class DataValidator:
    """
    Validates and cleans input data before processing.
    Ensures schema correctness and data quality.
    """

    REQUIRED_COLUMNS: List[str] = ["user_id", "expected_revenue"]

    # -------------------------------
    # 🔹 MAIN VALIDATION METHOD
    # -------------------------------
    def validate(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Starting data validation...")

        df = self._check_dataframe(df)
        df = self._check_required_columns(df)
        df = self._convert_types(df)
        df = self._remove_invalid_rows(df)
        df = self._remove_duplicates(df)

        df = df.reset_index(drop=True)

        logger.info("Data validation completed")
        return df

    # -------------------------------
    # 🔹 CHECK DATAFRAME
    # -------------------------------
    def _check_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        if not isinstance(df, pd.DataFrame):
            logger.error("Input is not a DataFrame")
            raise ValueError(ErrorMessages.INVALID_INPUT)

        if df.empty:
            logger.error("DataFrame is empty")
            raise ValueError(ErrorMessages.EMPTY_DATA)

        return df

    # -------------------------------
    # 🔹 CHECK REQUIRED COLUMNS
    # -------------------------------
    def _check_required_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        missing = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]

        if missing:
            logger.error(f"Missing columns: {missing}")
            raise ValueError(ErrorMessages.MISSING_COLUMNS)

        return df

    # -------------------------------
    # 🔹 TYPE CONVERSION
    # -------------------------------
    def _convert_types(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        df["user_id"] = df["user_id"].astype(str)

        df["expected_revenue"] = pd.to_numeric(
            df["expected_revenue"],
            errors="coerce"
        )

        return df

    # -------------------------------
    # 🔹 REMOVE INVALID DATA
    # -------------------------------
    def _remove_invalid_rows(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_count = len(df)

        df = df.dropna(subset=["expected_revenue"])
        df = df[df["expected_revenue"] >= 0]

        removed = initial_count - len(df)

        if removed > 0:
            logger.warning(f"Removed {removed} invalid rows")

        return df

    # -------------------------------
    # 🔹 REMOVE DUPLICATES
    # -------------------------------
    def _remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        before = len(df)

        df = df.drop_duplicates(subset=["user_id"], keep="first")

        removed = before - len(df)

        if removed > 0:
            logger.warning(f"Removed {removed} duplicate rows")

        return df