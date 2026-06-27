"""
Collaboration Runtime

Coordinates task delegation among
multiple SentinelAI agents.
"""

import time

from models.agent_result import AgentResult
from models.agent_task import AgentTask
from runtime.agent_registry import AgentRegistry


class CollaborationRuntime:
    """
    Multi-agent orchestration runtime.
    """

    def __init__(self):

        self.registry = AgentRegistry()

    def execute(
        self,
        task: AgentTask,
    ) -> AgentResult:

        start = time.perf_counter()

        agent = self.registry.find_agent(task)

        if agent is None:

            elapsed = (time.perf_counter() - start) * 1000

            return AgentResult(
                success=False,
                agent_name="None",
                task_id=task.id,
                output={},
                reasoning="No suitable agent found.",
                execution_time_ms=elapsed,
            )

        task.assigned_agent = agent.name

        result = agent.execute(task)

        return result
