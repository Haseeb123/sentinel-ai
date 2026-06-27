# SentinelAI Architecture

```

User

↓

Planner Agent

↓

Action

↓

Governance Runtime

├── Risk Engine

├── Policy Engine

├── Audit Engine

├── Security Engine (future)

├── Approval Engine (future)

↓

Execution Runtime

↓

Execution Agent

↓

MCP Tool Server

↓

Tool

↓

Response

```

---

## Runtime Layers

### Planning

Responsible for deciding *what* should happen.

### Governance

Responsible for deciding *whether* it should happen.

### Execution

Responsible for actually performing the action.

---

## Design Principles

- Single Responsibility
- Plugin Architecture
- Event Driven
- Observable
- Auditable
- Extensible