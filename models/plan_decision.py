"""
Plan Decision Model

Represents the governance decision for an
entire execution plan.
"""

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class PlanDecision(BaseModel):
    """
    Result of validating a generated plan.
    """

    allowed: bool = True

    overall_risk: str = "low"

    overall_confidence: float = 1.0

    approval_required: bool = False

    rejected_steps: list[int] = Field(default_factory=list)

    warnings: list[str] = Field(default_factory=list)

    reason: str = "Plan approved."

    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
