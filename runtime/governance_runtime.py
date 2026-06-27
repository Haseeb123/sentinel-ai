"""
Governance Runtime
"""

from models.action import Action
from models.decision import Decision

from runtime.audit_engine import AuditEngine
from runtime.policy_engine import PolicyEngine
from runtime.risk_engine import RiskEngine


class GovernanceRuntime:

    def __init__(self):

        self.engines = [

            RiskEngine(),

            PolicyEngine(),

            AuditEngine(),

        ]

    def process(self, action: Action) -> Decision:

        for engine in self.engines:

            action = engine.evaluate(action)

        if not action.policy_allowed:

            return Decision(

                allowed=False,

                reason="Blocked by governance policy.",

                approval_required=True,

                risk_score=action.risk_score

            )

        return Decision(

            allowed=True,

            reason="Approved",

            approval_required=action.approval_required,

            risk_score=action.risk_score

        )