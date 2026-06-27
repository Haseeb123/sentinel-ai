"""
Custom exceptions for SentinelAI.
"""


class SentinelRuntimeError(Exception):
    """Base runtime exception."""


class PolicyViolation(SentinelRuntimeError):
    """Raised when a policy blocks execution."""


class RiskThresholdExceeded(SentinelRuntimeError):
    """Raised when risk exceeds configured limits."""