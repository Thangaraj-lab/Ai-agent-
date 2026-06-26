# services/report_service.py

from typing import List, Dict
import pandas as pd
from pathlib import Path

from utils.logger import get_logger


logger = get_logger(__name__)


class ReportService:
    """
    Generates reports in different formats (CSV, Excel).
    """

    def generate_csv(self, users: List[Dict], path: str) -> str:
        """
        Save report as CSV.
        """

        logger.info("Generating CSV report...")

        df = pd.DataFrame(users)
        file_path = Path(path) / "report.csv"

        df.to_csv(file_path, index=False)

        return str(file_path)

    def generate_excel(self, users: List[Dict], path: str) -> str:
        """
        Save report as Excel.
        """

        logger.info("Generating Excel report...")

        df = pd.DataFrame(users)
        file_path = Path(path) / "report.xlsx"

        df.to_excel(file_path, index=False)

        return str(file_path)

    def generate_summary(self, users: List[Dict]) -> Dict:
        """
        Create summary stats for reports.
        """

        if not users:
            return {}

        return {
            "total_users": len(users),
            "avg_score": sum(u.get("score", 0) for u in users) / len(users),
            "max_score": max(u.get("score", 0) for u in users),
        }