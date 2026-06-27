"""
SentinelAI Application Entry Point.
"""

from fastapi import FastAPI

from agents.planner_agent import PlannerAgent
from backend.config import settings
from backend.responses import Metadata, TaskResponse
from backend.schemas import TaskRequest
from runtime.governance_runtime import GovernanceRuntime

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

planner = PlannerAgent()
runtime = GovernanceRuntime()


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "runtime": settings.VERSION,
    }


@app.post("/run-task", response_model=TaskResponse)
async def run_task(request: TaskRequest):

    action = planner.create_action(request.user_input)

    decision = runtime.process(action)

    return TaskResponse(
        action=action,
        decision=decision,
        metadata=Metadata(
            runtime_version=settings.VERSION
        ),
    )