"""
Project-wide exceptions.
"""


class SentinelAIException(Exception):
    """Base exception."""


class GovernanceException(SentinelAIException):
    """Governance failure."""


class PlanningException(SentinelAIException):
    """Planning failure."""


class ExecutionException(SentinelAIException):
    """Execution failure."""


class AgentException(SentinelAIException):
    """Agent execution failure."""
