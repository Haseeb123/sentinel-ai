"""
Base Tool Interface
"""

from abc import ABC, abstractmethod

from runtime.execution_context import ExecutionContext
from models.execution import ExecutionResult


class BaseTool(ABC):
    """
    Base class for every executable tool.
    """

    name: str = "base"

    description: str = ""

    version: str = "1.0"

    requires_approval: bool = False

    @abstractmethod
    def execute(
        self,
        context: ExecutionContext
    ) -> ExecutionResult:
        """
        Execute the tool.
        """
        raise NotImplementedError