"""
File Writer Tool
"""

import time
from pathlib import Path

from models.execution import ExecutionResult
from runtime.execution_context import ExecutionContext
from tools.base_tool import BaseTool


class FileWriterTool(BaseTool):

    name = "writer"

    description = "Write reports to disk."

    version = "1.0"

    requires_approval = False

    OUTPUT_DIRECTORY = Path("outputs")

    def execute(self, context: ExecutionContext) -> ExecutionResult:

        start = time.perf_counter()

        self.OUTPUT_DIRECTORY.mkdir(exist_ok=True)

        filename = context.action.parameters.get(
            "filename",
            "report.txt",
        )

        content = context.action.parameters.get(
            "content",
            "",
        )

        path = self.OUTPUT_DIRECTORY / filename

        path.write_text(
            content,
            encoding="utf-8",
        )

        elapsed = (time.perf_counter() - start) * 1000

        return ExecutionResult(
            success=True,
            tool=self.name,
            output=f"Saved to {path}",
            execution_time_ms=elapsed,
        )
