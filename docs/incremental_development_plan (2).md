# Incremental Development Plan

Group 14 · AI Energy Consumption Forecasting Dashboard

## How to read this plan

We build the system in small steps. Each capability has two versions:

- **Design version (`-design`)**: diagrams, contracts and a test plan. No code.
- **Working version**: the code, written by the coding agent, reviewed by us and tested.

Every version is tagged in GitHub **after** its pull request is merged into `main`. Branches are never deleted.

**Scope for Oral Examination 1:** only `v0.1.0-design` and `v0.1.0`. Everything after that is planned work.

## Plan

| Version | Type | Capability / Scope | Deliverable / Evidence | Requirements / Design Links |
|---|---|---|---|---|
| v0.1.0-design | Design | Problem, requirements and architecture | requirements, use cases, C4, sequence diagrams, ERD, dataset analysis, this plan | FR-01–FR-16, NFR-01–NFR-08, `uml/` |
| v0.1.0 | Working | Project setup | folder layout, dependency file, config, dataset in `data/raw/`, `scripts/check_env.py`, run steps in README | [architecture.md](architecture.md), `uml/c4/*` |
| v0.2.0-design | Design | Data ingestion | data flow diagram, validation rules, test plan | FR-01, SD-01, ERD |
| v0.2.0 | Working | Ingestion job | download, validate and load CSV into SQLite, tests | `src/backend/ingest/`, `tests/unit`, `tests/integration` |
| v0.3.0-design | Design | Measurements API | component view, endpoint contract, test plan | FR-02, FR-04, NFR-01, NFR-03 |
| v0.3.0 | Working | Measurements API | `/api/measurements`, `/api/measurements/summary`, API tests | `src/backend/app/api/`, `tests/integration` |
| v0.4.0-design | Design | History dashboard | page layout, chart list, UI test scenarios | FR-03, FR-04 |
| v0.4.0 | Working | History dashboard | history page with charts and summaries, system test | `src/frontend/`, `tests/system` |
| v0.5.0-design | Design | ML pipeline | final `ml_pipeline.md` (features, split, metrics) | FR-05, FR-06 |
| v0.5.0 | Working | ML training | training script, baseline vs model report, saved model | `src/ml/`, `tests/ml` |
| v0.6.0-design | Design | Prediction service | class diagram, `/predict` contract | FR-07, FR-08 |
| v0.6.0 | Working | Prediction API | `/api/predict`, `/api/predictions`, tests | `src/backend/app/services/`, `tests/` |
| v0.7.0-design | Design | Actual vs predicted | activity diagram, metric definitions | FR-09, FR-10 |
| v0.7.0 | Working | Comparison | `/api/compare`, comparison page, tests | `tests/system` |
| v0.8.0-design | Design | What-if and replay | replay state diagram | FR-11–FR-13 |
| v0.8.0 | Working | What-if and replay | what-if form, live replay, tests | `src/frontend/` |
| v0.9.0-design | Design | Alerts and reports | alert rules, report layout, deployment view | FR-14–FR-16 |
| v0.9.0 | Working | Alerts and reports | threshold alerts, alert log, report + CSV export, tests | `tests/` |
| v1.0.0 | Final | Integrated release | final diagrams, full traceability, run instructions, PDF report | all |

## Status

| Version | Status |
|---|---|
| v0.1.0-design | Done when its pull requests are merged and the tag is pushed |
| v0.1.0 | To finish before Oral Examination 1 (checklist below) |
| v0.2.0-design onward | Planned, not started |

## What each increment means

### v0.1.0-design: Design baseline (Oral Exam 1)
- **Question:** Do we understand the problem and have an architecture for the whole system?
- **Tools:** Mermaid, Markdown, Claude Code.
- **Done when:** every requirement has an ID, every diagram has an editable source and a PNG, the traceability matrix lists every requirement, all pull requests are reviewed and merged, and the tag is on the merged commit.

### v0.1.0: Project setup (Oral Exam 1)
- **Question:** Can every team member run the project on their own computer?
- **Tools:** Python 3.11, pip, venv.
- **Done when:**
  - folders `src/`, `tests/`, `data/`, `config/` exist as planned
  - `requirements.txt` installs without errors
  - the dataset is in `data/raw/` and is **not** committed (it is in `.gitignore`)
  - `python scripts/check_env.py` runs and reports the Python version, the packages and that the dataset file is found
  - the run steps in the README work on a clean checkout
  - a pull request is reviewed, merged and tagged

### v0.2.0: Data ingestion
- **Question:** Can we load the dataset reliably and repeatably?
- **Tools:** pandas, SQLAlchemy/SQLite, pytest.
- **Done when:** all 19,735 rows load, re-running adds no duplicates, a bad file is rejected, tests pass.

### v0.3.0: Measurements API
- **Question:** Can any component ask for historical data over HTTP?
- **Tools:** FastAPI, Pydantic, pytest.
- **Done when:** a date range returns exactly the expected rows, summaries are correct, invalid input returns 422, tests pass.

### v0.4.0: History dashboard
- **Question:** Can a user explore the historical data?
- **Tools:** HTML/JavaScript, Plotly.js.
- **Done when:** at least 3 charts render for a chosen date range and a system test passes.

### v0.5.0: ML training
- **Question:** Can a model predict energy better than simple baselines?
- **Tools:** scikit-learn, joblib.
- **Done when:** models are evaluated against the mean, median and persistence baselines on the chronological test split, and the best model is saved and reloads.

### v0.6.0: Prediction API
- **Question:** Can any component request a prediction?
- **Tools:** FastAPI, joblib.
- **Done when:** `/api/predict` returns a value in Wh, invalid input returns 422, a missing model returns 503, predictions are stored, tests pass.

### v0.7.0: Comparison
- **Question:** How close are predictions to actual values?
- **Done when:** the chart overlays actual and predicted values and MAE/RMSE/R² match an offline calculation.

### v0.8.0: What-if and replay
- **Question:** How does energy change with conditions, and does the system work on a live-like stream?
- **Done when:** the what-if form returns a prediction and replay streams readings with pause, resume and stop.

### v0.9.0: Alerts and reports
- **Question:** Can managers be warned and get a report?
- **Done when:** a reading above the threshold (default 400 Wh) creates one alert, and the report and CSV export work.

### v1.0.0: Final release
- **Question:** Does everything work end to end?
- **Done when:** the instructor's v1.0.0 checklist is met.

## Tests by increment

Tests are written by the coding agent and ship with the working version they check.

| Version | Test type | What it checks |
|---|---|---|
| v0.1.0 | Environment check | `scripts/check_env.py` passes |
| v0.2.0 | Unit, integration | file validation, full load, no duplicates |
| v0.3.0 | Unit, integration | summaries, date range, error codes |
| v0.4.0 | System | user picks dates and sees charts |
| v0.5.0 | Model evaluation | models vs baselines |
| v0.6.0 | Component, integration | prediction service and API |
| v0.7.0 | Unit, system | metrics and comparison page |
| v0.8.0 | Integration, system | what-if and replay flows |
| v0.9.0 | Unit, integration | alert rules and reports |
