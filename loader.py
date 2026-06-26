from typing import Union
import pandas as pd
from pathlib import Path
from utils.logger import get_logger
from app.config import settings

# engine/data/loader.py




logger = get_logger(__name__)


class DataLoader:
    """
    Responsible for loading data from multiple sources
    (CSV, Excel, JSON, API input).
    """

    def load(self, source: Union[str, list, dict]) -> pd.DataFrame:
        """
        Main entry point for loading data.
        """

        logger.info("Loading data...")

        if isinstance(source, str):
            return self._load_from_file(source)

        elif isinstance(source, list):
            return self._load_from_list(source)

        elif isinstance(source, dict):
            return self._load_from_dict(source)

        else:
            raise ValueError("Unsupported data source type")

    # -------------------------------
    # 🔹 FILE LOADER
    # -------------------------------
    def _load_from_file(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)

        if not path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"{file_path} does not exist")

        if path.suffix == ".csv":
            df = pd.read_csv(path)

        elif path.suffix in [".xlsx", ".xls"]:
            df = pd.read_excel(path)

        elif path.suffix == ".json":
            df = pd.read_json(path)

        else:
            raise ValueError("Unsupported file format")

        self._validate_not_empty(df)
        return df

    # -------------------------------
    # 🔹 LIST LOADER
    # -------------------------------
    def _load_from_list(self, data: list) -> pd.DataFrame:
        df = pd.DataFrame(data)
        self._validate_not_empty(df)
        return df

    # -------------------------------
    # 🔹 DICT LOADER
    # -------------------------------
    def _load_from_dict(self, data: dict) -> pd.DataFrame:
        df = pd.DataFrame([data])
        self._validate_not_empty(df)
        return df

    # -------------------------------
    # 🔹 VALIDATION
    # -------------------------------
    def _validate_not_empty(self, df: pd.DataFrame):
        if df.empty:
            logger.error("Loaded data is empty")
            raise ValueError("Input data is empty")

        logger.info(f"Data loaded successfully: {len(df)} records")