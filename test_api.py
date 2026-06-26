# tests/test_api.py

from fastapi.testclient import TestClient

from api.server import app


client = TestClient(app)


# -------------------------------
# 🔹 TEST HEALTH ENDPOINT
# -------------------------------
def test_health():
    response = client.get("/health/")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "ok"


# -------------------------------
# 🔹 TEST ANALYZE ENDPOINT
# -------------------------------
def test_analyze():
    payload = {
        "users": [
            {"user_id": "U1", "expected_revenue": 1000},
            {"user_id": "U2", "expected_revenue": 2000}
        ]
    }

    response = client.post("/ask/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "all_users" in data
    assert "top_users" in data


# -------------------------------
# 🔹 TEST USERS ROUTE
# -------------------------------
def test_users_enrich():
    payload = [
        {"user_id": "U1", "expected_revenue": 1000}
    ]

    response = client.post("/users/enrich", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "roi" in data[0]


# -------------------------------
# 🔹 TEST COMPANY SUMMARY
# -------------------------------
def test_company_summary():
    payload = [
        {"user_id": "U1", "mean": 1500, "risk": 200}
    ]

    response = client.post("/company/summary", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert "total_users" in data


# -------------------------------
# 🔹 INVALID INPUT TEST
# -------------------------------
def test_invalid_input():
    payload = {
        "users": [
            {"user_id": "U1", "expected_revenue": -100}
        ]
    }

    response = client.post("/ask/", json=payload)

    # Depending on validation, could be 400 or 200 cleaned
    assert response.status_code in [200, 400]