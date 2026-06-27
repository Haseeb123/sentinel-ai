"""
Base Agent

Every SentinelAI agent inherits from this class.
"""

from abc import ABC, abstractmethod

from models.agent_result import AgentResult
from models.agent_task import AgentTask


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def execute(
        self,
        task: AgentTask,
    ) -> AgentResult:
        """
        Execute a delegated task.
        """
        raise NotImplementedError

    def can_handle(
        self,
        task: AgentTask,
    ) -> bool:
        """
        Determine whether this agent
        can process the task.
        """

        return True
