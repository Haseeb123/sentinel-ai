"""
Represents a high-level task.
"""

from uuid import uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    description: str

    steps: list[str] = Field(default_factory=list)