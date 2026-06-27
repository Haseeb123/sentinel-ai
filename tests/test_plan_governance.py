from models.plan import Plan
from models.plan_step import PlanStep
from runtime.plan_governance import PlanGovernance


def test_safe_plan():

    governance = PlanGovernance()

    plan = Plan(
        goal="Summarize document",
        intent="summarize_document",
        confidence=0.96,
        risk="low",
        tools=[
            "pdf",
            "knowledge",
        ],
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
                description="Generate summary",
            ),
        ],
    )

    decision = governance.evaluate(plan)

    assert decision.allowed
    assert decision.reason == "Plan approved."


def test_unknown_tool():

    governance = PlanGovernance()

    plan = Plan(
        goal="Unknown tool",
        intent="test",
        confidence=0.95,
        risk="low",
        tools=["magic"],
        steps=[
            PlanStep(
                id=1,
                action="Do magic",
                tool="magic",
                description="Invalid tool",
            ),
        ],
    )

    decision = governance.evaluate(plan)

    assert not decision.allowed
    assert 1 in decision.rejected_steps


def test_high_risk_action():

    governance = PlanGovernance()

    plan = Plan(
        goal="Delete everything",
        intent="delete",
        confidence=0.95,
        risk="high",
        tools=["knowledge"],
        steps=[
            PlanStep(
                id=1,
                action="Delete all files",
                tool="knowledge",
                description="Dangerous",
            ),
        ],
    )

    decision = governance.evaluate(plan)

    assert not decision.allowed
    assert decision.approval_required


def test_low_confidence():

    governance = PlanGovernance()

    plan = Plan(
        goal="Unknown request",
        intent="unknown",
        confidence=0.55,
        risk="medium",
        tools=["knowledge"],
        steps=[
            PlanStep(
                id=1,
                action="Try something",
                tool="knowledge",
                description="Uncertain",
            ),
        ],
    )

    decision = governance.evaluate(plan)

    assert decision.approval_required
