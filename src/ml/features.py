"""Feature engineering (FR-05). See docs/ml_pipeline.md section 3. Implemented in v0.2.0."""
TIME_FEATURES = ["hour", "weekday", "is_weekend", "hour_sin", "hour_cos"]
LAG_FEATURES = ["lag_1", "lag_2", "lag_3", "rolling_mean_6"]


def add_time_features(df):
    """Add the TIME_FEATURES columns derived from the timestamp."""
    raise NotImplementedError("v0.2.0")


def add_lag_features(df):
    """Add past-only lags of Appliances; must never use the current or a future value."""
    raise NotImplementedError("v0.2.0")
