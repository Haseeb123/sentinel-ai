"""
Application configuration.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "SentinelAI"

    VERSION: str = "0.4.0"

    GEMINI_API_KEY: str

    MODEL_NAME: str = "gemini-2.5-flash"

    class Config:

        env_file = ".env"


settings = Settings()
