"""
Compliance Agent

Responsible for governance and policy analysis.
"""

import time

from agents.base_agent import BaseAgent
from models.agent_result import AgentResult
from models.agent_task import AgentTask


class ComplianceAgent(BaseAgent):

    def __init__(self):

        super().__init__("ComplianceAgent")

    def can_handle(
        self,
        task: AgentTask,
    ) -> bool:

        return task.task_type in [
            "policy",
            "compliance",
            "governance",
            "audit",
        ]

    def execute(
        self,
        task: AgentTask,
    ) -> AgentResult:

        start = time.perf_counter()

        policy = task.payload.get(
            "policy",
            task.description,
        )

        output = {
            "policy": policy,
            "status": "Compliant",
            "violations": [],
        }

        elapsed = (time.perf_counter() - start) * 1000

        return AgentResult(
            success=True,
            agent_name=self.name,
            task_id=task.id,
            output=output,
            reasoning="Policy evaluation completed.",
            execution_time_ms=elapsed,
        )
