"""
Workflow Task Model

Represents a high-level workflow generated
from a user's request. This workflow can
later be decomposed into multiple AgentTasks.
"""

from uuid import uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    """
    High-level workflow.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    title: str

    description: str

    status: str = "pending"

    steps: list[str] = Field(default_factory=list)
