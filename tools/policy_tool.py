"""
Policy Tool

Reads governance policies.
"""

import json
import time
from pathlib import Path

from models.execution import ExecutionResult
from runtime.execution_context import ExecutionContext
from tools.base_tool import BaseTool


class PolicyTool(BaseTool):

    name = "policy"

    description = "Read governance policies."

    version = "1.0"

    requires_approval = False

    POLICY_FILE = Path("policies/governance_policy.json")

    def execute(
        self,
        context: ExecutionContext
    ) -> ExecutionResult:

        start = time.perf_counter()

        if self.POLICY_FILE.exists():

            with open(
                self.POLICY_FILE,
                "r",
                encoding="utf8",
            ) as file:

                policy = json.load(file)

            output = json.dumps(
                policy,
                indent=2,
            )

        else:

            output = "Policy file not found."

        elapsed = (time.perf_counter() - start) * 1000

        return ExecutionResult(
            success=True,
            tool=self.name,
            output=output,
            execution_time_ms=elapsed,
        )