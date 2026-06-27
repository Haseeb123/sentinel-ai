"""
Plan Governance

Coordinates governance validation for
LLM-generated execution plans.
"""

from models.plan import Plan
from models.plan_decision import PlanDecision
from runtime.plan_validator import PlanValidator


class PlanGovernance:
    """
    Governs complete execution plans.
    """

    def __init__(self):

        self.validator = PlanValidator()

    def evaluate(
        self,
        plan: Plan,
    ) -> PlanDecision:
        """
        Evaluate an execution plan.
        """

        decision = self.validator.validate(plan)

        return decision
