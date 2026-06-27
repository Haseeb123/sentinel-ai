"""
Writer Agent

Responsible for producing reports
and formatted outputs.
"""

import time

from agents.base_agent import BaseAgent
from models.agent_result import AgentResult
from models.agent_task import AgentTask


class WriterAgent(BaseAgent):

    def __init__(self):

        super().__init__("WriterAgent")

    def can_handle(
        self,
        task: AgentTask,
    ) -> bool:

        return task.task_type in [
            "write",
            "report",
            "export",
        ]

    def execute(
        self,
        task: AgentTask,
    ) -> AgentResult:

        start = time.perf_counter()

        filename = task.payload.get(
            "filename",
            "output.txt",
        )

        output = {
            "filename": filename,
            "message": "Document generated successfully.",
        }

        elapsed = (time.perf_counter() - start) * 1000

        return AgentResult(
            success=True,
            agent_name=self.name,
            task_id=task.id,
            output=output,
            reasoning="Document generation completed.",
            execution_time_ms=elapsed,
        )
