"""Application settings (Backend API container). Override with environment variables."""
import os
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv("EFD_DATABASE_URL", f"sqlite:///{ROOT / 'data' / 'energy.db'}")
    model_path: Path = field(
        default_factory=lambda: Path(os.getenv("EFD_MODEL_PATH", str(ROOT / "models" / "energy_model.joblib")))
    )
    alert_threshold_wh: float = float(os.getenv("EFD_ALERT_THRESHOLD_WH", "400"))  # FR-14, decision D-06
    max_chart_points: int = int(os.getenv("EFD_MAX_CHART_POINTS", "5000"))  # NFR-01


settings = Settings()
