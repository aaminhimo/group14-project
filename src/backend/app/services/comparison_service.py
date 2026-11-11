"""Align actual and predicted values and compute error metrics (FR-09, FR-10). Implemented in v0.4.0.

Layer: services (business logic, no HTTP).
"""


class ComparisonService:
    """Planned operation: compare(start, end) -> {series, metrics}; reuses stored predictions and fills gaps."""
