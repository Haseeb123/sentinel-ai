"""
Task Decomposer

Converts an execution plan into a list
of AgentTasks for the collaboration runtime.
"""

from models.agent_task import AgentTask
from models.plan import Plan


class TaskDecomposer:

    TOOL_MAPPING = {
        "knowledge": "research",
        "policy": "compliance",
        "writer": "write",
        "pdf": "research",
    }

    def decompose(
        self,
        plan: Plan,
    ) -> list[AgentTask]:

        tasks = []

        for step in plan.steps:

            task_type = self.TOOL_MAPPING.get(
                step.tool,
                "research",
            )

            task = AgentTask(
                task_type=task_type,
                description=step.description,
                payload={
                    "action": step.action,
                    "tool": step.tool,
                    "parameters": step.parameters,
                },
            )

            tasks.append(task)

        return tasks
