"""
Execution Agent

Chooses the appropriate execution tool.
"""

from runtime.execution_context import ExecutionContext


class ExecutionAgent:

    def choose_tool(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        intent = context.action.intent.lower()

        request = context.action.user_request.lower()

        # ---------- PDF ----------

        if ".pdf" in request:

            context.selected_tool = "pdf"

            return context

        # ---------- Policy ----------

        if any(
            word in request
            for word in [
                "policy",
                "governance",
                "compliance",
                "rule",
            ]
        ):

            context.selected_tool = "policy"

            return context

        # ---------- File Writing ----------

        if any(
            word in request
            for word in [
                "save",
                "write",
                "export",
                "report",
            ]
        ):

            context.selected_tool = "writer"

            return context

        # ---------- Knowledge ----------

        context.selected_tool = "knowledge"

        return context