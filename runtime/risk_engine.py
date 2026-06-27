"""
Risk Engine

Calculates the risk score associated
with an Action.
"""

from models.action import Action
from runtime.base_engine import BaseEngine


class RiskEngine(BaseEngine):
    """Assigns a risk score to an action."""

    def evaluate(self, action: Action) -> Action:

        intent = action.intent

        if intent == "delete":
            action.risk_score = 95

        elif intent == "send_email":
            action.risk_score = 55

        elif intent == "summarize":
            action.risk_score = 15

        elif intent == "search":
            action.risk_score = 10

        else:
            action.risk_score = 25

        action.approval_required = action.risk_score >= 70

        return action