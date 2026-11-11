"""Pydantic request/response schemas (API contract: docs/architecture/c4_container.md)."""
from datetime import datetime

from pydantic import BaseModel, Field


class MeasurementPoint(BaseModel):
    timestamp: datetime
    values: dict[str, float]


class PredictRequest(BaseModel):
    """What-if input (FR-07, FR-11). Ranges come from docs/dataset/dataset_analysis.md section 3.

    The full list of indoor and weather fields is finalised at v0.3.0-design.
    """

    timestamp: datetime
    lights_wh: float = Field(0, ge=0, le=100)
    t_out: float = Field(..., ge=-20, le=45)
    rh_out: float = Field(..., ge=0, le=100)


class PredictResponse(BaseModel):
    predicted_wh: float
    unit: str = "Wh"
    model_version: str
