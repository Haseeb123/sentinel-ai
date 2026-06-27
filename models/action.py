"""
Action Model

Represents one executable action travelling
through the SentinelAI Governance Runtime.
"""

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Action(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    created_at: datetime = Field(default_factory=datetime.utcnow)

    user_request: str

    intent: str = "unknown"

    tool: str | None = None

    parameters: dict = Field(default_factory=dict)

    risk_score: int = 0

    approval_required: bool = False

    policy_allowed: bool = True

    security_flags: list[str] = Field(default_factory=list)

    status: str = "created"