"""
Execution Runtime

Coordinates execution using the Tool Registry.
"""

from agents.execution_agent import ExecutionAgent
from models.execution import ExecutionResult
from runtime.execution_context import ExecutionContext

from tools.tool_registry import ToolRegistry

from tools.knowledge_tool import KnowledgeTool
from tools.policy_tool import PolicyTool
from tools.pdf_reader_tool import PDFReaderTool
from tools.file_writer_tool import FileWriterTool


class ExecutionRuntime:
    """
    Coordinates execution.
    """

    def __init__(self):

        self.agent = ExecutionAgent()

        self.registry = ToolRegistry()

        self.registry.register(KnowledgeTool())
        self.registry.register(PolicyTool())
        self.registry.register(PDFReaderTool())
        self.registry.register(FileWriterTool())

    def execute(
        self,
        context: ExecutionContext
    ) -> ExecutionResult:

        context = self.agent.choose_tool(context)

        tool = self.registry.get(context.selected_tool)

        if tool is None:

            return ExecutionResult(
                success=False,
                tool=context.selected_tool,
                output=f"Tool '{context.selected_tool}' not registered.",
                execution_time_ms=0,
            )

        return tool.execute(context)