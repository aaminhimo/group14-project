"""Save and load the model artifact (Model Artifact Store container).

save() is implemented in v0.2.0; load() is implemented in v0.3.0 for the API.
"""
from pathlib import Path

DEFAULT_MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "energy_model.joblib"


def save(artifact: dict, path: Path = DEFAULT_MODEL_PATH) -> None:
    raise NotImplementedError("v0.2.0")


def load(path: Path = DEFAULT_MODEL_PATH) -> dict:
    """Raise FileNotFoundError if the file is missing; the API maps that to HTTP 503 (NFR-03)."""
    raise NotImplementedError("v0.3.0")
