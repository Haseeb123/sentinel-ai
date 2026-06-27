from models.action import Action

from runtime.policy_engine import PolicyEngine


def test_delete_blocked():

    action = Action(
        user_request="Delete",
        intent="delete"
    )

    engine = PolicyEngine()

    result = engine.evaluate(action)

    assert result.policy_allowed is False