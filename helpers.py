from typing import List, Dict, Any
import numpy as np
from app.constants import DEFAULT_TOP_K

# -------------------------------
# 🔹 SAFE DIVISION
# -------------------------------
def safe_divide(a: float, b: float) -> float:
    """
    Avoid division by zero errors.
    """
    return a / b if b != 0 else 0.0


# -------------------------------
# 🔹 NORMALIZE VALUES
# -------------------------------
def normalize(values: List[float]) -> List[float]:
    """
    Normalize values between 0 and 1.
    """
    if not values:
        return []

    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        return [0.5 for _ in values]

    return [(v - min_val) / (max_val - min_val) for v in values]


# -------------------------------
# 🔹 CALCULATE MEAN
# -------------------------------
def calculate_mean(values: List[float]) -> float:
    return float(np.mean(values)) if values else 0.0


# -------------------------------
# 🔹 CALCULATE STD DEV
# -------------------------------
def calculate_std(values: List[float]) -> float:
    return float(np.std(values)) if values else 0.0


# -------------------------------
# 🔹 TOP K SELECTOR
# -------------------------------
def get_top_k(items: List[Dict[str, Any]], key: str, k: int = DEFAULT_TOP_K):
    """
    Returns top-k items sorted by key.
    """
    return sorted(items, key=lambda x: x.get(key, 0), reverse=True)[:k]


# -------------------------------
# 🔹 VALIDATE LIST INPUT
# -------------------------------
def validate_list(data: Any) -> List:
    """
    Ensure input is a list.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    return data


# -------------------------------
# 🔹 ROUND FLOATS
# -------------------------------
def round_float(value: float, precision: int = 2) -> float:
    return round(value, precision)


# -------------------------------
# 🔹 BATCH PROCESSING
# -------------------------------
def chunk_data(data: List[Any], chunk_size: int):
    """
    Yield chunks of data for batch processing.
    """
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]