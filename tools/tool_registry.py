"""
Tool Registry

Maintains every available execution tool.
"""

from typing import Dict

from tools.base_tool import BaseTool


class ToolRegistry:
    """
    Central registry for execution tools.
    """

    def __init__(self):

        self._tools: Dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):

        self._tools[tool.name] = tool

    def unregister(self, name: str):

        if name in self._tools:
            del self._tools[name]

    def get(self, name: str):

        return self._tools.get(name)

    def exists(self, name: str):

        return name in self._tools

    def list_tools(self):

        return sorted(self._tools.keys())

    def count(self):

        return len(self._tools)