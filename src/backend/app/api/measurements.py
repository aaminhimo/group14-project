"""Router: measurements (FR-02, FR-04; sequence SD-02). Implemented in v0.1.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["measurements"])


@router.get("/measurements")
def get_measurements(start: str, end: str, fields: str | None = None):
    """Return readings between start and end for the requested fields (FR-02)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.1.0")


@router.get("/measurements/summary")
def get_summary(start: str, end: str):
    """Min/mean/max per variable for the range (FR-04)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.1.0")
