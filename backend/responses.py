"""
Response Models
"""

from datetime import datetime, timezone

from pydantic import BaseModel, Field

from models.action import Action
from models.decision import Decision
from models.execution import ExecutionResult
from models.plan import Plan
from models.plan_decision import PlanDecision


class Metadata(BaseModel):

    runtime_version: str

    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TaskResponse(BaseModel):

    action: Action | None = None

    plan: Plan | None = None

    decision: Decision | None = None

    plan_decision: PlanDecision | None = None

    execution: ExecutionResult | None = None

    metadata: Metadata
