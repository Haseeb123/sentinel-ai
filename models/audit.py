"""
Audit Record Model.
"""

from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class AuditRecord(BaseModel):

    id: str = Field(default_factory=lambda: str(uuid4()))

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    action_id: str

    event: str

    details: dict = Field(default_factory=dict)