"""
Application Entry Point.
"""

from fastapi import FastAPI

from backend.config import settings

app = FastAPI(

    title=settings.APP_NAME,

    version=settings.VERSION,

)


@app.get("/")
async def root():

    return {

        "application": settings.APP_NAME,

        "version": settings.VERSION,

        "status": "running"

    }