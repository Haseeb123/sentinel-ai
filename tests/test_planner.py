from agents.planner_agent import PlannerAgent


def test_summarize():

    planner = PlannerAgent()

    action = planner.create_action(
        "Summarize quarterly report"
    )

    assert action.intent == "summarize"


def test_delete():

    planner = PlannerAgent()

    action = planner.create_action(
        "Delete customer records"
    )

    assert action.intent == "delete"