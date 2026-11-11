"""Validate the CSV and load it into the measurements table (FR-01, sequence SD-01). Implemented in v0.1.0.

Rules from docs/dataset/dataset_analysis.md:
- exactly the 29 expected columns; rv1/rv2 are dropped (decision D-01)
- timestamps parse and are unique, otherwise the file is rejected (D-02)
- idempotent: re-running inserts no duplicates
"""
EXPECTED_COLUMNS = [
    "date", "Appliances", "lights",
    "T1", "RH_1", "T2", "RH_2", "T3", "RH_3", "T4", "RH_4", "T5", "RH_5",
    "T6", "RH_6", "T7", "RH_7", "T8", "RH_8", "T9", "RH_9",
    "T_out", "Press_mm_hg", "RH_out", "Windspeed", "Visibility", "Tdewpoint",
    "rv1", "rv2",
]
DROPPED_COLUMNS = ["rv1", "rv2"]


def validate(df) -> None:
    """Raise ValueError if the dataframe breaks any schema rule."""
    raise NotImplementedError("v0.1.0")


def load(csv_path) -> int:
    """Load valid rows into the database and return the number of new rows."""
    raise NotImplementedError("v0.1.0")
