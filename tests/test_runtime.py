from agents.planner_agent import PlannerAgent

from runtime.governance_runtime import GovernanceRuntime


def test_runtime():

    planner = PlannerAgent()

    runtime = GovernanceRuntime()

    action = planner.create_action(
        "Summarize report"
    )

    decision = runtime.process(action)

    assert decision.allowed is True