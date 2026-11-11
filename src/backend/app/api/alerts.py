"""Router: alerts (FR-15). Implemented in v0.6.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["alerts"])


@router.get("/alerts")
def list_alerts(limit: int = 100):
    """Alert log, newest first."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.6.0")
