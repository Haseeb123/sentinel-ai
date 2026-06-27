"""
Central logging for SentinelAI.
"""

import logging
from pathlib import Path

LOG_DIR = Path("data/audit_logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "sentinel.log"

logger = logging.getLogger("SentinelAI")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler = logging.FileHandler(LOG_FILE)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.handlers.clear()

logger.addHandler(file_handler)

logger.addHandler(console_handler)