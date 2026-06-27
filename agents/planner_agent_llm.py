"""
Planner Agent (LLM)

Uses Gemini to generate structured execution plans.
"""

from pathlib import Path

from llm.gemini_client import GeminiClient
from models.plan import Plan


class PlannerAgentLLM:

    PROMPT_FILE = Path("prompts/planner_prompt.txt")

    def __init__(self):

        self.client = GeminiClient()

        self.system_prompt = self.PROMPT_FILE.read_text(encoding="utf8")

    def create_plan(
        self,
        user_request: str,
    ) -> Plan:

        prompt = f"""
{self.system_prompt}

User Request:

{user_request}
"""

        return self.client.generate_plan(prompt)
