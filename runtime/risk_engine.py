"""
Risk Engine

Calculates a risk score for an action.
"""

from config.thresholds import HIGH_RISK_SCORE, LOW_RISK_SCORE
from runtime.base_engine import BaseEngine


class RiskEngine(BaseEngine):

    def evaluate(self, action):

        text = action.user_request.lower()

        high_risk_keywords = [
            "delete",
            "erase",
            "remove",
            "shutdown",
            "drop",
        ]

        if any(keyword in text for keyword in high_risk_keywords):

            action.risk_score = HIGH_RISK_SCORE

            action.approval_required = True

        else:

            action.risk_score = LOW_RISK_SCORE

        return action
