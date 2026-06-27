"""
SentinelAI Application Entry Point

This module initializes the FastAPI application and exposes the REST API
for interacting with the SentinelAI Governance Runtime.
"""

from fastapi import FastAPI

from backend.config import settings
from backend.schemas import TaskRequest
from backend.responses import TaskResponse, Metadata

from agents.planner_agent import PlannerAgent

from runtime.governance_runtime import GovernanceRuntime
from runtime.execution_runtime import ExecutionRuntime
from runtime.execution_context import ExecutionContext


# -----------------------------------------------------------------------------
# FastAPI App
# -----------------------------------------------------------------------------

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="SentinelAI - Governance Runtime for Safe AI Agents"
)

# -----------------------------------------------------------------------------
# Initialize Components
# -----------------------------------------------------------------------------

planner = PlannerAgent()

governance_runtime = GovernanceRuntime()

execution_runtime = ExecutionRuntime()


# -----------------------------------------------------------------------------
# Root Endpoint
# -----------------------------------------------------------------------------

@app.get("/")
async def root():
    """
    Root endpoint.
    """

    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }


# -----------------------------------------------------------------------------
# Health Check
# -----------------------------------------------------------------------------

@app.get("/health")
async def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "runtime_version": settings.VERSION
    }


# -----------------------------------------------------------------------------
# Main Task Endpoint
# -----------------------------------------------------------------------------

@app.post(
    "/run-task",
    response_model=TaskResponse
)
async def run_task(request: TaskRequest):
    """
    Main pipeline.

    User Request
        ↓
    Planner Agent
        ↓
    Governance Runtime
        ↓
    Execution Runtime
        ↓
    Response
    """

    # -------------------------------------------------------------
    # Step 1 — Planning
    # -------------------------------------------------------------

    action = planner.create_action(request.user_input)

    # -------------------------------------------------------------
    # Step 2 — Governance
    # -------------------------------------------------------------

    decision = governance_runtime.process(action)

    # -------------------------------------------------------------
    # Step 3 — Create Execution Context
    # -------------------------------------------------------------

    context = ExecutionContext(
        action=action,
        decision=decision,
    )

    # -------------------------------------------------------------
    # Step 4 — Execute (Only if Allowed)
    # -------------------------------------------------------------

    execution_result = None

    if decision.allowed:
        execution_result = execution_runtime.execute(context)

    # -------------------------------------------------------------
    # Step 5 — Return Response
    # -------------------------------------------------------------

    return TaskResponse(
        action=action,
        decision=decision,
        execution=execution_result,
        metadata=Metadata(
            runtime_version=settings.VERSION
        )
    )