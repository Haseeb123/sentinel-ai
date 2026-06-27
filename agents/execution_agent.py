"""
Execution Agent

Chooses the appropriate execution tool.
"""

from config.constants import DEFAULT_TOOL
from runtime.execution_context import ExecutionContext


class ExecutionAgent:

    TOOL_MAPPING = {
        "summarize": "knowledge",
        "search": "knowledge",
        "lookup": "knowledge",
        "policy": "policy",
        "compliance": "policy",
        "governance": "policy",
        "write": "writer",
        "report": "writer",
    }

    def choose_tool(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        intent = context.action.intent.lower()

        context.selected_tool = self.TOOL_MAPPING.get(
            intent,
            DEFAULT_TOOL,
        )

        return context
