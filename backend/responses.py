
"""
Standard API response models.
"""

from datetime import datetime, timezone

from pydantic import BaseModel, Field

from models.action import Action
from models.decision import Decision


class Metadata(BaseModel):
    runtime_version: str = "0.1.0"

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class TaskResponse(BaseModel):
    action: Action
    decision: Decision
    metadata: Metadata