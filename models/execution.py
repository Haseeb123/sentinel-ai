"""
Execution Models
"""

from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class ExecutionResult(BaseModel):
    """
    Result returned after executing a tool.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    success: bool

    tool: str

    output: str

    execution_time_ms: float

    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
