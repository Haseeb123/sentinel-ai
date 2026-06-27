from runtime.risk_engine import RiskEngine
from runtime.policy_engine import PolicyEngine


class GovernanceRuntime:

    def __init__(self):

        self.risk = RiskEngine()

        self.policy = PolicyEngine()

    def evaluate(self, plan):

        risk = self.risk.score(plan)

        policy = self.policy.check(plan)

        return {

            "risk_score": risk,

            "allowed": policy,

            "approval_required": risk > 70
        }