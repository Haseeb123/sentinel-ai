"""
Research Agent

Responsible for searching, retrieving,
and summarizing knowledge.
"""

import time

from agents.base_agent import BaseAgent
from models.agent_result import AgentResult
from models.agent_task import AgentTask


class ResearchAgent(BaseAgent):

    def __init__(self):

        super().__init__("ResearchAgent")

    def can_handle(
        self,
        task: AgentTask,
    ) -> bool:

        return task.task_type in [
            "research",
            "search",
            "lookup",
            "summarize",
        ]

    def execute(
        self,
        task: AgentTask,
    ) -> AgentResult:

        start = time.perf_counter()

        query = task.payload.get(
            "query",
            task.description,
        )

        output = {
            "query": query,
            "summary": f"Research completed for '{query}'.",
            "sources": [],
        }

        elapsed = (time.perf_counter() - start) * 1000

        return AgentResult(
            success=True,
            agent_name=self.name,
            task_id=task.id,
            output=output,
            reasoning="Knowledge lookup completed.",
            execution_time_ms=elapsed,
        )
