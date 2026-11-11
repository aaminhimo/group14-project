"""Router: reports (FR-16). Implemented in v0.6.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["reports"])


@router.get("/reports/summary")
def summary_report(start: str, end: str, format: str = "json"):
    """Integrated report (trends, error metrics, alerts) as JSON or CSV."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.6.0")
