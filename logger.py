# utils/logger.py

import logging
import sys
from typing import Optional
from app.config import settings


class LoggerFactory:
    """
    Factory class to create and manage loggers.
    Ensures consistent logging format across the application.
    """

    _loggers = {}

    @classmethod
    def get_logger(cls, name: str) -> logging.Logger:
        """
        Returns a configured logger instance.
        Uses singleton pattern per logger name.
        """

        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(cls._get_log_level())

        # Prevent duplicate handlers
        if not logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(cls._get_formatter())
            logger.addHandler(handler)

        logger.propagate = False
        cls._loggers[name] = logger

        return logger

    @staticmethod
    def _get_log_level() -> int:
        level_map = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        return level_map.get(settings.LOG_LEVEL.upper(), logging.INFO)

    @staticmethod
    def _get_formatter() -> logging.Formatter:
        return logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )


# -------------------------------
# 🔥 Helper shortcut function
# -------------------------------
def get_logger(name: Optional[str] = "app") -> logging.Logger:
    return LoggerFactory.get_logger(name)