"""
Planner Agent

Converts natural language into
a structured Action.
"""

from models.action import Action


class PlannerAgent:
    """Simple planner for Sprint 1."""

    def create_action(self, user_request: str) -> Action:

        action = Action(user_request=user_request)

        text = user_request.lower()

        if any(word in text for word in ["delete", "remove", "erase"]):
            action.intent = "delete"

        elif any(word in text for word in ["summarize", "summary"]):
            action.intent = "summarize"

        elif any(word in text for word in ["email", "send"]):
            action.intent = "send_email"

        elif any(word in text for word in ["search", "find"]):
            action.intent = "search"

        else:
            action.intent = "general"

        return action
