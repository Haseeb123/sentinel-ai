"""
PDF Reader Tool
"""

import time

from models.execution import ExecutionResult
from runtime.execution_context import ExecutionContext
from tools.base_tool import BaseTool
from tools.document_loader import DocumentLoader


class PDFReaderTool(BaseTool):

    name = "pdf"

    description = "Read PDF documents."

    version = "1.0"

    requires_approval = False

    def __init__(self):

        self.loader = DocumentLoader()

    def execute(self, context: ExecutionContext) -> ExecutionResult:

        start = time.perf_counter()

        file_path = context.action.parameters.get("file_path")

        if not file_path:

            return ExecutionResult(
                success=False,
                tool=self.name,
                output="No file_path supplied.",
                execution_time_ms=0,
            )

        try:

            content = self.loader.load(file_path)

            elapsed = (time.perf_counter() - start) * 1000

            return ExecutionResult(
                success=True,
                tool=self.name,
                output=content,
                execution_time_ms=elapsed,
            )

        except Exception as exc:

            elapsed = (time.perf_counter() - start) * 1000

            return ExecutionResult(
                success=False,
                tool=self.name,
                output=str(exc),
                execution_time_ms=elapsed,
            )
