from pydantic import BaseModel
from typing import List

class TaskRequest(BaseModel):
    user_input: str

class TaskStep(BaseModel):
    step: str

class GovernanceResult(BaseModel):
    allowed: bool
    risk_score: int
    approval_required: bool
    message: str