"""
Agent Result Model
"""

from datetime import datetime, timezone

from pydantic import BaseModel, Field


class AgentResult(BaseModel):
    """
    Result produced by an agent.
    """

    success: bool = True

    agent_name: str

    task_id: str

    output: dict = Field(default_factory=dict)

    reasoning: str = ""

    warnings: list[str] = Field(default_factory=list)

    execution_time_ms: float = 0.0

    completed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
