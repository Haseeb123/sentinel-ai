"""
SentinelAI Application

FastAPI entry point for the SentinelAI Governance Runtime.
"""

from fastapi import FastAPI

from utils.logger import get_logger

from backend.config import settings
from backend.schemas import TaskRequest
from backend.responses import (
    TaskResponse,
    Metadata,
)

from agents.planner_agent import PlannerAgent
from agents.planner_agent_llm import PlannerAgentLLM

from runtime.governance_runtime import GovernanceRuntime
from runtime.execution_runtime import ExecutionRuntime
from runtime.execution_context import ExecutionContext
from runtime.plan_governance import PlanGovernance


# -----------------------------------------------------------------------------
# Logger
# -----------------------------------------------------------------------------

logger = get_logger(__name__)


# -----------------------------------------------------------------------------
# FastAPI App
# -----------------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)


# -----------------------------------------------------------------------------
# Components
# -----------------------------------------------------------------------------

legacy_planner = PlannerAgent()

llm_planner = PlannerAgentLLM()

governance_runtime = GovernanceRuntime()

plan_governance = PlanGovernance()

execution_runtime = ExecutionRuntime()


# -----------------------------------------------------------------------------
# Root Endpoint
# -----------------------------------------------------------------------------

@app.get("/")
async def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running",
    }


# -----------------------------------------------------------------------------
# Health Endpoint
# -----------------------------------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "runtime_version": settings.VERSION,
    }


# -----------------------------------------------------------------------------
# Main Endpoint
# -----------------------------------------------------------------------------

@app.post(
    "/run-task",
    response_model=TaskResponse,
)
async def run_task(
    request: TaskRequest,
):
    """
    Complete SentinelAI execution pipeline.

    User Request
        ↓
    Legacy Planner
        ↓
    Governance Runtime
        ↓
    Gemini Planner
        ↓
    Plan Governance
        ↓
    Execution Runtime
        ↓
    Response
    """

    logger.info(f"Received request: {request.user_input}")

    # -------------------------------------------------------------
    # Legacy Planner
    # -------------------------------------------------------------

    action = legacy_planner.create_action(
        request.user_input
    )

    decision = governance_runtime.process(
        action
    )

    # -------------------------------------------------------------
    # Gemini Planner
    # -------------------------------------------------------------

    plan = llm_planner.create_plan(
        request.user_input
    )

    plan_decision = plan_governance.evaluate(
        plan
    )

    logger.info(
        f"Governance allowed={decision.allowed}, "
        f"Plan allowed={plan_decision.allowed}"
    )

    execution = None

    # -------------------------------------------------------------
    # Execute
    # -------------------------------------------------------------

    if decision.allowed and plan_decision.allowed:

        context = ExecutionContext(
            action=action,
            decision=decision,
        )

        execution = execution_runtime.execute(
            context
        )

    else:

        logger.warning(
            "Execution blocked by governance."
        )

    logger.info("Task completed successfully.")

    # -------------------------------------------------------------
    # Response
    # -------------------------------------------------------------

    return TaskResponse(

        action=action,

        plan=plan,

        decision=decision,

        plan_decision=plan_decision,

        execution=execution,

        metadata=Metadata(
            runtime_version=settings.VERSION,
        ),
    )