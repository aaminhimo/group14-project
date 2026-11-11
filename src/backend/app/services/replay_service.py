"""Replay historical readings as a simulated live stream (FR-12, FR-13). Implemented in v0.5.0.

Layer: services (business logic, no HTTP).
"""


class ReplayService:
    """Planned operations: start(start_ts, speed, threshold), next(session_id), set_status(session_id, status)."""
