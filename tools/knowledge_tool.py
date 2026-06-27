"""
Knowledge Tool

Provides access to SentinelAI's internal knowledge.
"""

import time

from models.execution import ExecutionResult
from runtime.execution_context import ExecutionContext
from tools.base_tool import BaseTool


class KnowledgeTool(BaseTool):

    name = "knowledge"

    description = "Search enterprise knowledge."

    version = "1.0"

    requires_approval = False

    def execute(
        self,
        context: ExecutionContext
    ) -> ExecutionResult:

        start = time.perf_counter()

        query = context.action.user_request

        output = (
            f"Knowledge search completed.\n\n"
            f"Query:\n{query}\n\n"
            f"(Knowledge base integration will be added in Sprint 3.)"
        )

        elapsed = (time.perf_counter() - start) * 1000

        return ExecutionResult(
            success=True,
            tool=self.name,
            output=output,
            execution_time_ms=elapsed,
        )