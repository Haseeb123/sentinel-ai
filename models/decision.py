"""
Decision Model

Represents the governance decision
returned after evaluating an Action.
"""

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Decision(BaseModel):
    """Final governance decision."""

    allowed: bool

    reason: str

    approval_required: bool

    risk_score: int

    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
