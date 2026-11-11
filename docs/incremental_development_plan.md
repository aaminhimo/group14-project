# Incremental Development Plan

> Group 14 · AI Energy Consumption Forecasting Dashboard · Format from the instructor's §2.1

**Tag convention.** `vX.Y.0-design` is the merged design checkpoint for a capability. `vX.Y.0` is the merged, tested, working implementation of the same capability. `v1.0.0` is the final integrated release. Tags are created only on merged commits in `main`.

**Change from the draft plan:** the separate `v0.0.1-docs` tag was folded into `v0.1.0-design`. The architecture baseline (requirements, C4 L1/L2, container sequence diagrams, ERD, dataset analysis) was finished together with the Increment 1 design.

| Version | Type | Capability / Scope | Deliverable / Evidence | Requirements / Design Links |
|---|---|---|---|---|
| v0.1.0-design | Design | Architecture baseline + data ingestion & historical dashboard | requirements, C4 L1/L2, SD-01…SD-05, ERD, dataset analysis, code skeleton | FR-01–FR-04, [architecture.md](architecture.md), `uml/c4/*`, `uml/sequence/*`, `uml/data/erd.mmd` |
| v0.1.0 | Working | Load CSV into SQLite; query by date range; history charts | ingest job, `/api/measurements`, history page, tests | `src/backend/ingest/`, `src/backend/app/api/measurements.py`, `tests/unit`, `tests/integration` |
| v0.2.0-design | Design | ML pipeline | `ml_pipeline.md` final: features, split, metrics, artifact format | FR-05, FR-06, [ml_pipeline.md](ml_pipeline.md) |
| v0.2.0 | Working | Features, training, evaluation, saved model | training script, baseline vs models report | `src/ml/`, `tests/ml` |
| v0.3.0-design | Design | Prediction service | component view, class diagram, `/predict` contract | FR-07, FR-08, `uml/c4/c4_component.mmd`, `uml/class/` |
| v0.3.0 | Working | Prediction API + stored predictions | `/api/predict`, `/api/predictions`, API tests | `src/backend/app/services/prediction_service.py`, `tests/integration` |
| v0.4.0-design | Design | Actual vs predicted comparison | activity diagram, metric definitions | FR-09, FR-10, SD-04 |
| v0.4.0 | Working | Comparison chart, error summary, date filters | `/api/compare`, comparison page, tests | `src/backend/app/services/comparison_service.py`, `tests/system` |
| v0.5.0-design | Design | What-if and simulated live replay | replay state diagram, SD-03/SD-05 refined | FR-11–FR-13 |
| v0.5.0 | Working | What-if form; replay with next-step predictions | `/api/replay*`, what-if + replay pages, tests | `src/backend/app/services/replay_service.py`, `src/frontend/` |
| v0.6.0-design | Design | Alerts and integrated reporting | alert rules, report layout, deployment view | FR-14–FR-16, `uml/deployment/` |
| v0.6.0 | Working | Threshold alerts, alert log, report + CSV export | `/api/alerts`, `/api/reports/summary`, tests | `src/backend/app/services/alert_service.py`, `report_service.py` |
| v1.0.0 | Final | Integrated release | final diagrams, full traceability, run instructions, `se_report_group_14.pdf` | all |

## Details per increment

### v0.1.0: Data ingestion and historical dashboard
- **Main question:** Can a user explore historical energy and environmental data?
- **Tools:** pandas, SQLAlchemy/SQLite, FastAPI, Plotly.js, pytest + httpx.
- **Acceptance criteria:** all 19,735 rows load with no loss; re-run inserts 0 duplicates; a date-range query returns exactly the expected rows; ≥ 3 charts render; unit and integration tests pass.

### v0.2.0: ML pipeline
- **Main question:** Can we predict appliance energy better than naive baselines?
- **Tools:** pandas, scikit-learn (LinearRegression, RandomForest, GradientBoosting), joblib.
- **Acceptance criteria:** chronological split documented; mean and persistence baselines reported (persistence test MAE ≈ 26.7 Wh); the chosen next-step model beats persistence and the what-if model beats the mean on test MAE; model and metrics saved and reloadable.

### v0.3.0: Prediction API
- **Main question:** Can any component request a prediction?
- **Tools:** FastAPI, Pydantic, joblib, pytest + httpx.
- **Acceptance criteria:** `/api/predict` validates input and returns a value in Wh with the model version; invalid input returns 422; missing model returns 503; the response equals the offline model output for the same input; the prediction is stored.

### v0.4.0: Comparison
- **Main question:** How close are predictions to actual values?
- **Tools:** FastAPI, Plotly.js.
- **Acceptance criteria:** chart overlays actual and predicted; MAE/RMSE/R² for the chosen period match an offline calculation within 0.01.

### v0.5.0: What-if and replay
- **Main question:** How does energy change with conditions, and does the system work on a live-like stream?
- **Tools:** FastAPI, Plotly.js.
- **Acceptance criteria:** the what-if form returns a prediction; replay emits readings at the configured speed; pause/resume/stop work; the live chart updates.

### v0.6.0: Alerts and reporting
- **Main question:** Can managers be warned and get a report?
- **Tools:** FastAPI, pandas (CSV export).
- **Acceptance criteria:** a reading above threshold creates exactly one alert, which is visible in the log; the report shows trends, errors and alerts; the CSV export opens correctly.

### v1.0.0: Integrated release
- **Main question:** Does everything work end to end?
- **Acceptance criteria:** the instructor's 11-point v1.0.0 checklist (§14 of the instructions).
