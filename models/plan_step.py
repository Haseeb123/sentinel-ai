"""
Plan Step Model
"""

from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    """
    Represents one execution step produced by the planner.
    """

    id: int

    action: str

    tool: str

    description: str = ""

    parameters: dict = Field(default_factory=dict)
