"""
Execution Context

Carries state across the execution pipeline.
"""

from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field

from models.action import Action
from models.decision import Decision


class ExecutionContext(BaseModel):
    """
    Shared context for one execution run.
    """

    run_id: str = Field(default_factory=lambda: str(uuid4()))

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    action: Action

    decision: Decision | None = None

    selected_tool: str | None = None

    execution_started: datetime | None = None

    execution_finished: datetime | None = None

    metadata: dict = Field(default_factory=dict)