from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def plan(self, task):

        return [
            "Understand request",
            "Identify tools",
            "Request governance approval",
            "Execute task"
        ]