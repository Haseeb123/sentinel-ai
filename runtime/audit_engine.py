"""
Audit Engine
"""

import json
from pathlib import Path

from models.action import Action
from models.audit import AuditRecord
from observability.logger import logger


class AuditEngine:

    OUTPUT = Path("data/audit_logs/audit.jsonl")

    def evaluate(self, action: Action) -> Action:

        record = AuditRecord(
            action_id=action.id,
            engine="AuditEngine",
            message=f"Action evaluated ({action.intent})",
        )

        self.OUTPUT.parent.mkdir(parents=True, exist_ok=True)

        with open(self.OUTPUT, "a", encoding="utf8") as file:
            file.write(record.model_dump_json() + "\n")

        logger.info(record.message)

        return action
