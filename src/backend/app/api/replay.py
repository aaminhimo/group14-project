"""Router: replay (FR-12, FR-13, FR-14; sequence SD-05). Implemented in v0.5.0."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["replay"])


@router.post("/replay", status_code=201)
def start_replay():
    """Create a replay session with start time, speed and alert threshold (FR-12)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.5.0")


@router.get("/replay/{session_id}/next")
def next_reading(session_id: int):
    """Return the next reading, its next-step prediction and any alert (FR-13, FR-14)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.5.0")


@router.patch("/replay/{session_id}")
def update_replay(session_id: int):
    """Pause, resume or stop a session (FR-12)."""
    raise HTTPException(status_code=501, detail="Not implemented until v0.5.0")
