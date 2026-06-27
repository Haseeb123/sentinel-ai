"""
Central logging configuration.
"""

import logging

LOGGER_NAME = "SentinelAI"


def get_logger(name: str | None = None) -> logging.Logger:

    logger = logging.getLogger(name or LOGGER_NAME)

    if not logger.handlers:

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.setLevel(logging.INFO)

    return logger
