"""
Agent Registry

Maintains all available SentinelAI agents and
selects the appropriate one for a task.
"""

from agents.base_agent import BaseAgent
from agents.compliance_agent import ComplianceAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from models.agent_task import AgentTask


class AgentRegistry:
    """
    Registry of available agents.
    """

    def __init__(self):

        self.agents: list[BaseAgent] = [
            ResearchAgent(),
            ComplianceAgent(),
            WriterAgent(),
        ]

    def register(
        self,
        agent: BaseAgent,
    ):

        self.agents.append(agent)

    def find_agent(
        self,
        task: AgentTask,
    ) -> BaseAgent | None:
        """
        Return the first capable agent.
        """

        for agent in self.agents:

            if agent.can_handle(task):

                return agent

        return None

    def list_agents(self) -> list[str]:

        return [agent.name for agent in self.agents]
