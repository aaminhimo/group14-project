"""Router: predictions (FR-07, FR-08, NFR-03; sequence SD-03). Implemented in v0.3.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["predictions"])


@router.post("/predict")
def predict():
    """What-if prediction: 422 on invalid input, 503 if the model is missing (FR-07)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.3.0")


@router.get("/predictions")
def list_predictions(source: str | None = None, limit: int = 100):
    """Stored prediction history (FR-08)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.3.0")
