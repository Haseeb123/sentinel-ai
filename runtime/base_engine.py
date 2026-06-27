"""
Base class for all governance engines.
"""

from abc import ABC, abstractmethod

from models.action import Action


class BaseEngine(ABC):
    """Abstract base class for governance engines."""

    @abstractmethod
    def evaluate(self, action: Action) -> Action:
        """
        Evaluate or modify an Action.

        Returns:
            Updated Action
        """
        raise NotImplementedError
