"""
Plan Validator
"""

from config.constants import HIGH_RISK_ACTIONS, SUPPORTED_TOOLS
from config.thresholds import MIN_CONFIDENCE
from models.plan import Plan
from models.plan_decision import PlanDecision


class PlanValidator:

    def validate(
        self,
        plan: Plan,
    ) -> PlanDecision:

        decision = PlanDecision()

        decision.overall_risk = plan.risk

        decision.overall_confidence = plan.confidence

        # -----------------------------
        # Tool Validation
        # -----------------------------

        for step in plan.steps:

            if step.tool not in SUPPORTED_TOOLS:

                decision.allowed = False

                decision.rejected_steps.append(step.id)

                decision.warnings.append(f"Unsupported tool: {step.tool}")

        # -----------------------------
        # Action Validation
        # -----------------------------

        for step in plan.steps:

            action = step.action.lower()

            if any(keyword in action for keyword in HIGH_RISK_ACTIONS):

                decision.allowed = False

                decision.approval_required = True

                decision.rejected_steps.append(step.id)

                decision.warnings.append(f"High-risk action: {step.action}")

        # -----------------------------
        # Confidence Validation
        # -----------------------------

        if plan.confidence < MIN_CONFIDENCE:

            decision.approval_required = True

            decision.warnings.append("Planner confidence below threshold.")

        decision.reason = "Plan approved." if decision.allowed else "Plan rejected."

        return decision
