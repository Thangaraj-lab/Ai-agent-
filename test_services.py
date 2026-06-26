# tests/test_services.py

import pytest

from services.advisor_service import AdvisorService
from services.user_service import UserService
from services.company_service import CompanyService
from services.report_service import ReportService


# -------------------------------
# 🔹 TEST ADVISOR SERVICE
# -------------------------------
def test_advisor_service():
    service = AdvisorService()

    data = [
        {"user_id": "U1", "expected_revenue": 1000},
        {"user_id": "U2", "expected_revenue": 2000}
    ]

    result = service.analyze(data)

    assert "summary" in result
    assert "all_users" in result
    assert "top_users" in result


# -------------------------------
# 🔹 TEST USER SERVICE
# -------------------------------
def test_user_service():
    service = UserService()

    users = [
        {"user_id": "U1", "mean": 1000, "risk": 100, "score": 800}
    ]

    enriched = service.enrich_users(users)

    assert "roi" in enriched[0]
    assert "efficiency" in enriched[0]

    filtered = service.filter_users(enriched, min_score=500)
    assert len(filtered) > 0


# -------------------------------
# 🔹 TEST COMPANY SERVICE
# -------------------------------
def test_company_service():
    service = CompanyService()

    users = [
        {"user_id": "U1", "mean": 1500, "risk": 200}
    ]

    summary = service.summarize(users)

    assert summary["total_users"] == 1
    assert "avg_revenue" in summary

    top = service.get_top_performers(users, threshold=1000)
    assert len(top) == 1


# -------------------------------
# 🔹 TEST REPORT SERVICE
# -------------------------------
def test_report_service(tmp_path):
    service = ReportService()

    users = [
        {"user_id": "U1", "mean": 1500, "score": 1200}
    ]

    # CSV
    csv_path = service.generate_csv(users, tmp_path)
    assert "report.csv" in csv_path

    # Excel
    excel_path = service.generate_excel(users, tmp_path)
    assert "report.xlsx" in excel_path

    # Summary
    summary = service.generate_summary(users)
    assert "total_users" in summary


# -------------------------------
# 🔹 EDGE CASE
# -------------------------------
def test_empty_service():
    service = AdvisorService()

    with pytest.raises(Exception):
        service.analyze([])