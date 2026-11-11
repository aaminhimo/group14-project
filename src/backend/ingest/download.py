"""Download the UCI Appliances Energy Prediction dataset (Data Ingestion Job container, FR-01).

Usage from the repository root:  python -m src.backend.ingest.download
"""
import io
import urllib.request
import zipfile
from pathlib import Path

DATASET_URL = "https://archive.ics.uci.edu/static/public/374/appliances+energy+prediction.zip"
RAW_DIR = Path(__file__).resolve().parents[3] / "data" / "raw"
CSV_NAME = "energydata_complete.csv"


def download(dest_dir: Path = RAW_DIR) -> Path:
    """Download and extract the CSV, skipping the download if it already exists. Returns the CSV path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / CSV_NAME
    if target.exists():
        return target
    with urllib.request.urlopen(DATASET_URL, timeout=120) as resp:
        with zipfile.ZipFile(io.BytesIO(resp.read())) as archive:
            archive.extract(CSV_NAME, dest_dir)
    return target


if __name__ == "__main__":
    print(f"Dataset available at {download()}")
