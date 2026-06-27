from models.action import Action
from runtime.risk_engine import RiskEngine


def test_delete_high_risk():

    action = Action(user_request="Delete everything", intent="delete")

    engine = RiskEngine()

    result = engine.evaluate(action)

    assert result.risk_score == 95
