from pathlib import Path

from models.action import Action
from models.decision import Decision
from runtime.execution_context import ExecutionContext
from tools.document_loader import DocumentLoader
from tools.file_writer_tool import FileWriterTool


def test_document_loader_txt(tmp_path):

    file = tmp_path / "sample.txt"

    file.write_text(
        "SentinelAI Test",
        encoding="utf8",
    )

    loader = DocumentLoader()

    text = loader.load(str(file))

    assert text == "SentinelAI Test"


def test_file_writer_tool():

    action = Action(
        user_request="write report",
        parameters={
            "filename": "pytest_report.txt",
            "content": "hello world",
        },
    )

    decision = Decision(
        allowed=True,
        reason="Approved",
        approval_required=False,
        risk_score=0,
    )

    context = ExecutionContext(
        action=action,
        decision=decision,
    )

    tool = FileWriterTool()

    result = tool.execute(context)

    assert result.success

    output = Path("outputs/pytest_report.txt")

    assert output.exists()

    output.unlink()
