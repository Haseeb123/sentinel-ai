"""
Application-wide constants.
"""

APP_NAME = "SentinelAI"

DEFAULT_TOOL = "knowledge"

SUPPORTED_TOOLS = {
    "knowledge",
    "policy",
    "pdf",
    "writer",
}

HIGH_RISK_ACTIONS = {
    "delete",
    "remove",
    "erase",
    "drop",
    "shutdown",
}

SUPPORTED_INTENTS = {
    "summarize",
    "search",
    "lookup",
    "policy",
    "compliance",
    "governance",
    "write",
    "report",
    "export",
}
