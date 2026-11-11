"""Router: compare (FR-09, FR-10; sequence SD-04). Implemented in v0.4.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["compare"])


@router.get("/compare")
def compare(start: str, end: str):
    """Actual vs predicted series plus MAE, RMSE and R2 for the period."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.4.0")
