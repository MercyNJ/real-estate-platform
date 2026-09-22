from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Infrastructure health check.

    Deliberately not under /api/v1/: this is an operational probe, not a
    public API resource, so it is exempt from the API versioning rule in
    architecture.md.
    """
    return {"status": "ok"}
