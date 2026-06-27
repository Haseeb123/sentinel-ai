"""
API Request Schemas
"""

from pydantic import BaseModel


class TaskRequest(BaseModel):
    """Incoming user request."""

    user_input: str