from typing import List, Dict, Any
from utils.helpers import round_float
from app.constants import RiskLevel

# -------------------------------
# 🔹 FORMAT USER RESULT
# -------------------------------
def format_user_result(user: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format single user output for API/UI.
    """

    return {
        "user_id": user.get("user_id"),
        "mean": round_float(user.get("mean", 0)),
        "min": round_float(user.get("min", 0)),
        "max": round_float(user.get("max", 0)),
        "risk": round_float(user.get("risk", 0)),
        "risk_level": get_risk_level(user.get("risk", 0)),
        "score": round_float(user.get("score", 0)),
    }


# -------------------------------
# 🔹 FORMAT LIST OF USERS
# -------------------------------
def format_users(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [format_user_result(u) for u in users]


# -------------------------------
# 🔹 FORMAT FINAL RESPONSE
# -------------------------------
def format_response(all_users: List[Dict], top_users: List[Dict]) -> Dict:
    """
    Final structured response.
    """

    return {
        "summary": {
            "total_users": len(all_users),
            "top_selected": len(top_users),
        },
        "all_users": format_users(all_users),
        "top_users": format_users(top_users),
    }


# -------------------------------
# 🔹 RISK LEVEL CLASSIFIER
# -------------------------------
def get_risk_level(risk_value: float) -> str:
    """
    Convert numeric risk into category.
    """

    if risk_value < 50:
        return RiskLevel.LOW.value
    elif risk_value < 150:
        return RiskLevel.MODERATE.value
    else:
        return RiskLevel.HIGH.value


# -------------------------------
# 🔹 GENERATE DECISION TEXT
# -------------------------------
def build_decision_summary(top_users: List[Dict[str, Any]]) -> str:
    """
    Human-readable decision output.
    """

    if not top_users:
        return "No strong candidates found."

    best = top_users[0]

    return (
        f"Focus on user {best['user_id']} "
        f"for highest return ({round_float(best['mean'])}) "
        f"with manageable risk."
    )