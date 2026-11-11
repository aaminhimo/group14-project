"""Backend API container entry point.

Run from the repository root:  uvicorn src.backend.app.main:app --reload
Design: docs/architecture/c4_container.md (Backend API) and sequence diagrams SD-02..SD-05.
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.backend.app.api import alerts, compare, measurements, predictions, replay, reports

app = FastAPI(title="Group 14 - Energy Forecasting Dashboard API", version="0.1.0-design")

for module in (measurements, predictions, compare, replay, alerts, reports):
    app.include_router(module.router, prefix="/api")


@app.get("/api/health")
def health() -> dict:
    """Liveness check. `model_loaded` becomes meaningful in v0.3.0."""
    return {"status": "ok", "model_loaded": False}


FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
