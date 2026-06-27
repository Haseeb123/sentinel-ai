from models.plan import Plan
from models.plan_step import PlanStep
from runtime.task_decomposer import TaskDecomposer


def test_plan_decomposition():

    plan = Plan(
        goal="Summarize document",
        intent="summarize",
        confidence=0.96,
        risk="low",
        tools=["pdf", "knowledge", "writer"],
        steps=[
            PlanStep(
                id=1,
                action="Read PDF",
                tool="pdf",
                description="Read file",
            ),
            PlanStep(
                id=2,
                action="Summarize",
                tool="knowledge",
                description="Summarize document",
            ),
            PlanStep(
                id=3,
                action="Write Summary",
                tool="writer",
                description="Save summary",
            ),
        ],
    )

    tasks = TaskDecomposer().decompose(plan)

    assert len(tasks) == 3

    assert tasks[0].task_type == "research"

    assert tasks[1].task_type == "research"

    assert tasks[2].task_type == "write"
