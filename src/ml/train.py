"""Training pipeline CLI (ML Training Pipeline container; FR-06; sequence SD-01). Implemented in v0.2.0.

Usage:  python -m src.ml.train
Steps: load measurements -> features -> chronological 70/15/15 split -> baselines + candidate models
-> select on validation -> score the test set once -> save artifact + metrics -> insert a model_runs row.
"""
SPLIT = (0.70, 0.15, 0.15)
CANDIDATES = ["LinearRegression", "RandomForestRegressor", "GradientBoostingRegressor"]


def main() -> None:
    raise NotImplementedError("v0.2.0")


if __name__ == "__main__":
    main()
