"""
Policy Engine
"""

import json
from pathlib import Path

from models.action import Action
from runtime.base_engine import BaseEngine


class PolicyEngine(BaseEngine):

    POLICY_FILE = (
        Path(__file__).resolve().parent.parent / "data" / "configs" / "policies.json"
    )

    def __init__(self):

        if not self.POLICY_FILE.exists():
            raise FileNotFoundError(f"Policy file not found: {self.POLICY_FILE}")

        with open(self.POLICY_FILE, "r", encoding="utf-8") as file:
            self.policies = json.load(file)

    def evaluate(self, action: Action) -> Action:

        rule = self.policies.get(action.intent, self.policies["general"])

        action.policy_allowed = rule["allowed"]

        action.approval_required = action.approval_required or rule["approval_required"]

        return action
