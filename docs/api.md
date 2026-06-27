# SentinelAI API

## GET /

Returns runtime information.

Example

```json
{
    "application":"SentinelAI",
    "version":"0.1.0",
    "status":"running"
}
```

---

## GET /health

Returns health status.

---

## POST /run-task

Input

```json
{
    "user_input":"Summarize quarterly report"
}
```

Output

```json
{
    "action":{...},
    "decision":{...},
    "metadata":{...}
}
```