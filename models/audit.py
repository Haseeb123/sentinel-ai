"""
Audit Model
"""

from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class AuditRecord(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    action_id: str

    engine: str

    message: str

    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
