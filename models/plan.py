"""
Plan Model
"""

from pydantic import BaseModel, Field

from models.plan_step import PlanStep


class Plan(BaseModel):
    """
    Complete execution plan produced by Gemini.
    """

    goal: str

    intent: str

    confidence: float = 1.0

    risk: str

    tools: list[str] = Field(default_factory=list)

    steps: list[PlanStep] = Field(default_factory=list)
