"""ORM models: implements the ERD in uml/data/erd.mmd (docs/architecture/data_model.md).

Planned classes and the increment that implements each:
    Measurement    v0.1.0  FR-01, FR-02
    ModelRun       v0.2.0  FR-06
    Prediction     v0.3.0  FR-08
    ReplaySession  v0.5.0  FR-12
    Alert          v0.6.0  FR-14, FR-15
"""
from src.backend.app.db import Base  # noqa: F401  (the ORM classes above will subclass Base)
