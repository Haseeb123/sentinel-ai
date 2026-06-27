from models.action import Action
from models.decision import Decision
from runtime.execution_context import ExecutionContext
from tools.knowledge_tool import KnowledgeTool
from tools.policy_tool import PolicyTool
from tools.tool_registry import ToolRegistry


def test_registry_register():

    registry = ToolRegistry()

    registry.register(KnowledgeTool())

    assert registry.exists("knowledge")


def test_registry_count():

    registry = ToolRegistry()

    registry.register(KnowledgeTool())
    registry.register(PolicyTool())

    assert registry.count() == 2


def test_knowledge_tool():

    action = Action(user_request="Summarize company handbook", intent="summarize")

    decision = Decision(
        allowed=True,
        reason="Approved",
        approval_required=False,
        risk_score=10,
    )

    context = ExecutionContext(
        action=action,
        decision=decision,
    )

    tool = KnowledgeTool()

    result = tool.execute(context)

    assert result.success is True
