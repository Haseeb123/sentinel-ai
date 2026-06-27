"""
Global configuration for SentinelAI.
"""

from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = "SentinelAI"

    VERSION = "0.1.0"

    DEBUG = True

    API_PREFIX = "/api"


settings = Settings()