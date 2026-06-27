"""
Governance Decision Model.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class Decision(BaseModel):

    allowed: bool

    reason: str

    approval_required: bool

    risk_score: int

    evaluated_at: datetime = Field(default_factory=datetime.utcnow)