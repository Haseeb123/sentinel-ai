from models.agent_task import AgentTask
from runtime.collaboration_runtime import CollaborationRuntime


def test_research_agent():

    runtime = CollaborationRuntime()

    task = AgentTask(
        task_type="research",
        description="Research AI governance",
    )

    result = runtime.execute(task)

    assert result.success

    assert result.agent_name == "ResearchAgent"


def test_compliance_agent():

    runtime = CollaborationRuntime()

    task = AgentTask(
        task_type="compliance",
        description="Check ISO policy",
    )

    result = runtime.execute(task)

    assert result.success

    assert result.agent_name == "ComplianceAgent"


def test_writer_agent():

    runtime = CollaborationRuntime()

    task = AgentTask(
        task_type="write",
        description="Generate report",
    )

    result = runtime.execute(task)

    assert result.success

    assert result.agent_name == "WriterAgent"


def test_unknown_agent():

    runtime = CollaborationRuntime()

    task = AgentTask(
        task_type="video",
        description="Create video",
    )

    result = runtime.execute(task)

    assert not result.success
