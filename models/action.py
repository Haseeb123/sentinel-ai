"""
Action Model

Represents one executable action travelling
through the SentinelAI Governance Runtime.
"""

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class Action(BaseModel):
    """Represents a governed action inside SentinelAI."""

    id: str = Field(default_factory=lambda: str(uuid4()))

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user_request: str

    intent: str = "unknown"

    tool: str | None = None

    parameters: dict[str, Any] = Field(default_factory=dict)

    risk_score: int = 0

    approval_required: bool = False

    policy_allowed: bool = True

    security_flags: list[str] = Field(default_factory=list)

    status: str = "created"
