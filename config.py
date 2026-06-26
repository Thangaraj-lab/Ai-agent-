from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    """
    Central configuration for the entire application.
    Loads values from environment variables or .env file.
    """

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    # -------------------------------
    # 🔹 APP CONFIG
    # -------------------------------
    APP_NAME: str = "Agent AI"
    ENV: str = Field(default="dev")
    DEBUG: bool = True

    # -------------------------------
    # 🔹 API CONFIG
    # -------------------------------
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # -------------------------------
    # 🔹 DATA PATHS
    # -------------------------------
    RAW_DATA_PATH: str = "data/raw/"
    PROCESSED_DATA_PATH: str = "data/processed/"

    # -------------------------------
    # 🔹 SIMULATION CONFIG
    # -------------------------------
    SIMULATIONS: int = 2000
    RISK_FACTOR: float = 0.1

    # -------------------------------
    # 🔹 ML / PREDICTION CONFIG
    # -------------------------------
    MODEL_TYPE: str = "xgboost"

    # -------------------------------
    # 🔹 OPTIMIZATION CONFIG
    # -------------------------------
    MAX_ITERATIONS: int = 100

    # -------------------------------
    # 🔹 AGENT / LLM CONFIG
    # -------------------------------
    LLM_PROVIDER: str = "groq"
    LLM_MODEL: str = "mixtral-8x7b"
    LLM_API_KEY: Optional[str] = None

    # -------------------------------
    # 🔹 FEATURES
    # -------------------------------
    ENABLE_CACHE: bool = False
    ENABLE_MEMORY: bool = True

    # -------------------------------
    # 🔹 LOGGING
    # -------------------------------
    LOG_LEVEL: str = "INFO"


# -------------------------------
# 🔥 SINGLETON SETTINGS INSTANCE
# -------------------------------
@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()