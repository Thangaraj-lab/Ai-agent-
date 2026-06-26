from enum import Enum

# app/constants.py



# -------------------------------
# 🔹 ENV TYPES
# -------------------------------
class Environment(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "prod"


# -------------------------------
# 🔹 USER SEGMENTATION
# -------------------------------
class UserSegment(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    PREMIUM = "premium"


# -------------------------------
# 🔹 RISK LEVELS
# -------------------------------
class RiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


# -------------------------------
# 🔹 SCENARIO TYPES
# -------------------------------
class ScenarioType(str, Enum):
    BASE = "base"
    BULL = "bull"
    BEAR = "bear"


# -------------------------------
# 🔹 API ROUTES
# -------------------------------
class APIRoutes:
    ANALYZE = "/analyze"
    ASK = "/ask"
    USERS = "/users"
    COMPANY = "/company"
    HEALTH = "/health"


# -------------------------------
# 🔹 DEFAULT VALUES
# -------------------------------
DEFAULT_TOP_K = 3
DEFAULT_CONFIDENCE_LEVEL = 0.95


# -------------------------------
# 🔹 ERROR MESSAGES
# -------------------------------
class ErrorMessages:
    INVALID_INPUT = "Invalid input data"
    MISSING_COLUMNS = "Required columns are missing"
    EMPTY_DATA = "Input data is empty"
    INTERNAL_ERROR = "Something went wrong"


# -------------------------------
# 🔹 SUCCESS MESSAGES
# -------------------------------
class SuccessMessages:
    ANALYSIS_COMPLETE = "Analysis completed successfully"
    DATA_PROCESSED = "Data processed successfully"