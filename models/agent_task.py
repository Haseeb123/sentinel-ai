"""
Agent Task Model

Represents an executable unit of work
assigned to an individual agent.
"""

from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class AgentTask(BaseModel):
    """
    Individual task executed by an agent.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    task_type: str

    description: str

    payload: dict = Field(default_factory=dict)

    priority: int = 1

    assigned_agent: str | None = None

    parent_task_id: str | None = None

    status: str = "pending"
