import asyncio
import json

from app.main import app


def test_health_endpoint_returns_ok() -> None:
    """Smoke test for the Phase 0 health check endpoint.

    Invokes the ASGI application directly rather than using FastAPI's
    TestClient, since TestClient requires httpx and no new dependency has
    been approved for this step.
    """
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/health",
        "headers": [],
        "query_string": b"",
        "server": ("testserver", 80),
        "client": ("testclient", 123),
        "scheme": "http",
    }

    messages: list[dict] = []

    async def receive() -> dict:
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message: dict) -> None:
        messages.append(message)

    asyncio.run(app(scope, receive, send))

    start = next(m for m in messages if m["type"] == "http.response.start")
    body = next(m for m in messages if m["type"] == "http.response.body")

    assert start["status"] == 200
    assert json.loads(body["body"]) == {"status": "ok"}
