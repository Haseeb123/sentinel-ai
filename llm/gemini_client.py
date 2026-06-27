"""
Gemini Client

Provides communication with Google's Gemini model.
"""

import json
import os

from dotenv import load_dotenv
from google import genai

from models.plan import Plan


class GeminiClient:

    def __init__(self):

        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.model = os.getenv(
            "MODEL_NAME",
            "gemini-2.5-flash",
        )

        self.client = genai.Client(api_key=api_key)

    def generate_plan(
        self,
        prompt: str,
    ) -> Plan:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        text = response.text.strip()

        # Remove markdown code fences if present
        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        text = text.strip()

        data = json.loads(text)

        return Plan.model_validate(data)
