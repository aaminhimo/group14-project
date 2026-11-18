# Incremental Development Plan

> Group 14 · AI Energy Consumption Forecasting Dashboard · Format from the instructor's §2.1 · Plan revision for Oral Examination 1

**Tag convention.** `vX.Y.0-design` is the merged design checkpoint for a capability. `vX.Y.0` is the merged, tested, working implementation of the same capability. `v1.0.0` is the final integrated release. Tags are created only on merged commits in `main`, after the pull request is merged.

**Scope of this revision.** Phase 1 is split into a design checkpoint and a working checkpoint. `v0.1.0-design` contains only the design and documentation work that was actually done; `v0.1.0` is a small working project setup built on that design, with no API backend and no automated tests yet. The old single "v0.1.0" working increment (ingest job + API + history page + tests) was too large, so it is split into three small increments: ingestion (v0.2.0), measurements API (v0.3.0) and history dashboard (v0.4.0). Tests are not a separate phase: each working increment from v0.2.0 onward ships its own tests and is not complete until they pass (instructor §13); v0.1.0 has no executable features to test. All later increments are kept and renumbered.

## Plan

| Version | Type | Capability / Scope | Deliverable / Evidence | Requirements / Design Links |
|---|---|---|---|---|
| v0.1.0-design | Design | Phase 1: problem, requirements and architecture baseline | project description, requirements, use case diagram + descriptions, C4 L1/L2, SD-01…SD-05, ERD, dataset analysis, ML pipeline draft, this plan | FR-01–FR-16, NFR-01–NFR-08, [architecture.md](architecture.md), `uml/c4/*`, `uml/sequence/*`, `uml/data/erd.mmd`, `uml/usecase/*` |
| v0.1.0 | Working | Project setup: repository layout, dependency file, configuration, dataset in place, environment check | `src/` and `data/` layout, dependency file, config file, dataset in `data/raw/`, `scripts/check_env.py`, run instructions in `README.md` | [architecture.md](architecture.md), `uml/c4/*` (C4 L2) |
| v0.2.0-design | Design | Data ingestion design | DFD for ingestion, validation rules, ingestion test plan | FR-01, SD-01, ERD `measurements`, `uml/data/dfd.mmd` |
| v0.2.0 | Working | Ingestion job: download, validate, load CSV into SQLite | ingest job, DB schema, unit + integration tests, test report | `src/backend/ingest/`, `src/backend/app/models.py`, `tests/unit`, `tests/integration` |
| v0.3.0-design | Design | Measurements API design | backend component view, endpoint contract, API test plan | FR-02, FR-04 (summary), NFR-01, NFR-03, SD-02, `uml/c4/c4_component.mmd` |
| v0.3.0 | Working | Measurements API: date-range query, summary stats, downsampling | `/api/health`, `/api/measurements`, `/api/measurements/summary`, API tests | `src/backend/app/api/measurements.py`, `services/measurement_service.py`, `tests/unit`, `tests/integration` |
| v0.4.0-design | Design | History dashboard design | page layout/wireframe, chart list, UI test scenarios | FR-03, FR-04, SD-02 |
| v0.4.0 | Working | History page: date picker, energy and climate charts, summaries | history page, system test, test report | `src/frontend/`, `tests/system` |
| v0.5.0-design | Design | ML pipeline | `ml_pipeline.md` final: features, split, metrics, artifact format | FR-05, FR-06, [ml_pipeline.md](ml_pipeline.md) |
| v0.5.0 | Working | Features, training, evaluation, saved model | training script, baseline vs models report, model tests | `src/ml/`, `tests/ml` |
| v0.6.0-design | Design | Prediction service | class diagram, `/predict` contract | FR-07, FR-08, `uml/class/` |
| v0.6.0 | Working | Prediction API + stored predictions | `/api/predict`, `/api/predictions`, API tests | `src/backend/app/services/prediction_service.py`, `tests/component`, `tests/integration` |
| v0.7.0-design | Design | Actual vs predicted comparison | activity diagram, metric definitions | FR-09, FR-10, SD-04 |
| v0.7.0 | Working | Comparison chart, error summary, date filters | `/api/compare`, comparison page, tests | `src/backend/app/services/comparison_service.py`, `tests/system` |
| v0.8.0-design | Design | What-if and simulated live replay | replay state diagram, SD-03/SD-05 refined | FR-11–FR-13 |
| v0.8.0 | Working | What-if form; replay with next-step predictions | `/api/replay*`, what-if + replay pages, tests | `src/backend/app/services/replay_service.py`, `src/frontend/` |
| v0.9.0-design | Design | Alerts and integrated reporting | alert rules, report layout, deployment view | FR-14–FR-16, `uml/deployment/` |
| v0.9.0 | Working | Threshold alerts, alert log, report + CSV export | `/api/alerts`, `/api/reports/summary`, tests | `src/backend/app/services/alert_service.py`, `report_service.py` |
| v1.0.0 | Final | Integrated release | final diagrams, full traceability, run instructions, `se_report_group_14.pdf` | all |

## Status at Oral Examination 1

| Version | Status | Evidence |
|---|---|---|
| v0.1.0-design | **Done** once the Phase 1 PRs are merged and the tag is pushed | `docs/` and `uml/` on `main`, tag `v0.1.0-design` |
| v0.1.0 | Planned | Nothing implemented yet; `src/` is intentionally empty until this increment starts |
| v0.2.0-design onward | Planned | Not started |

Phase 1 contents:
- Project description, scope and assumptions A-01…A-05
- Requirements: FR-01…FR-16, NFR-01…NFR-08, use cases UC-01…UC-07
- Use case diagram and use case descriptions
- C4 Level 1 and Level 2
- Sequence diagrams SD-01…SD-05
- ERD
- Dataset analysis and ML pipeline draft
- Traceability matrix (all rows "Designed") and AI development log

## Details per increment

### v0.1.0-design: Phase 1 baseline
- **Main question:** Do we understand the problem and have an architecture that covers the whole system?
- **Tools:** Mermaid, Markdown, Claude Code (agent log in `docs/ai_development_log.md`).
- **Acceptance criteria:** every requirement has an ID; every diagram has an editable source and a rendered PNG; every requirement appears in the traceability matrix; all PRs reviewed and merged; tag on the merged commit.

### v0.1.0: Project setup
- **Main question:** Can every team member set up the same environment and find the dataset from a clean clone?
- **Tools:** Python, pandas, Git/GitHub.
- **Acceptance criteria:** the folder layout matches `architecture.md`; one documented command installs the dependencies; `scripts/check_env.py` confirms the Python version, the required packages and the presence of the dataset file; the run instructions in `README.md` work on a clean clone; tag on the merged commit.
- **Out of scope:** the API backend (starts in v0.3.0) and automated tests (start in v0.2.0).

### v0.2.0: Data ingestion
- **Main question:** Can the system load the dataset reliably and repeatably?
- **Tools:** pandas, SQLAlchemy/SQLite, pytest.
- **Acceptance criteria:** all 19,735 rows load with no loss; re-running inserts 0 duplicates; a CSV with 28 columns or bad timestamps is rejected; `rv1`/`rv2` are dropped; unit and integration tests pass.

### v0.3.0: Measurements API
- **Main question:** Can any component request historical data over HTTP?
- **Tools:** FastAPI, Pydantic, pytest + httpx.
- **Acceptance criteria:** a date-range query returns exactly the expected rows; summary returns min/mean/max; invalid parameters return 422; a one-month query returns in under 2 s; ranges above 5,000 points are downsampled; API tests pass.

### v0.4.0: History dashboard
- **Main question:** Can a user explore historical energy and environmental data?
- **Tools:** HTML/JavaScript, Plotly.js, FastAPI static files.
- **Acceptance criteria:** at least 3 charts render (energy, temperature, humidity); summaries are shown for the selected range; the system test opens the page, picks dates and finds data in the chart.

### v0.5.0: ML pipeline
- **Main question:** Can we predict appliance energy better than naive baselines?
- **Tools:** pandas, scikit-learn (LinearRegression, RandomForest, GradientBoosting), joblib.
- **Acceptance criteria:** chronological split documented; mean and persistence baselines reported (persistence test MAE ≈ 26.7 Wh); the chosen next-step model beats persistence and the what-if model beats the mean on test MAE; model and metrics saved and reloadable.

### v0.6.0: Prediction API
- **Main question:** Can any component request a prediction?
- **Tools:** FastAPI, Pydantic, joblib, pytest + httpx.
- **Acceptance criteria:** `/api/predict` validates input and returns a value in Wh with the model version; invalid input returns 422; missing model returns 503; the response equals the offline model output for the same input; the prediction is stored.

### v0.7.0: Comparison
- **Main question:** How close are predictions to actual values?
- **Tools:** FastAPI, Plotly.js.
- **Acceptance criteria:** chart overlays actual and predicted; MAE/RMSE/R² for the chosen period match an offline calculation within 0.01.

### v0.8.0: What-if and replay
- **Main question:** How does energy change with conditions, and does the system work on a live-like stream?
- **Tools:** FastAPI, Plotly.js.
- **Acceptance criteria:** the what-if form returns a prediction; replay emits readings at the configured speed; pause/resume/stop work; the live chart updates.

### v0.9.0: Alerts and reporting
- **Main question:** Can managers be warned and get a report?
- **Tools:** FastAPI, pandas (CSV export).
- **Acceptance criteria:** a reading above threshold creates exactly one alert, which is visible in the log; the report shows trends, errors and alerts; the CSV export opens correctly.

### v1.0.0: Integrated release
- **Main question:** Does everything work end to end?
- **Acceptance criteria:** the instructor's 11-point v1.0.0 checklist (§14 of the instructions).

## Tests by increment

| Version | Test level | Test file (planned) | Verifies |
|---|---|---|---|
| v0.2.0 | Unit | `tests/unit/test_loader_validation.py` | schema validation rejects bad files |
| v0.2.0 | Integration | `tests/integration/test_ingest.py` | full load, 0 duplicates on re-run |
| v0.3.0 | Unit | `tests/unit/test_summary_stats.py` | min/mean/max calculation |
| v0.3.0 | Integration | `tests/integration/test_measurements_api.py` | date range, 422 errors, downsampling |
| v0.4.0 | System | `tests/system/test_history_page.py` | user flow: pick dates, chart has data |
| v0.5.0 | Model evaluation | `tests/ml/test_model_quality.py` | models beat baselines (NFR-04) |
| v0.6.0 | Component, integration | `tests/component/test_prediction_service.py`, `tests/integration/test_predict_api.py` | prediction service and API |
| v0.7.0 | Unit, system | `tests/unit/test_metrics.py`, `tests/system/test_compare_page.py` | metrics and comparison page |
| v0.8.0 | Integration, system | `tests/integration/test_replay_api.py`, `tests/system/test_whatif_flow.py` | replay and what-if flows |
| v0.9.0 | Unit, integration | `tests/unit/test_alert_rules.py`, `tests/integration/test_alerts_api.py`, `tests/integration/test_reports_api.py` | alerts and reports |

## Mapping from the previous plan

| Previous | Now |
|---|---|
| v0.1.0-design | v0.1.0-design (reduced to what Phase 1 actually delivered) |
| v0.1.0 | reduced to a small project setup (v0.1.0); ingest, API and dashboard split into v0.2.0, v0.3.0, v0.4.0 |
| v0.2.0 | v0.5.0 |
| v0.3.0 | v0.6.0 |
| v0.4.0 | v0.7.0 |
| v0.5.0 | v0.8.0 |
| v0.6.0 | v0.9.0 |
| v1.0.0 | v1.0.0 |

When this plan is merged, update the "Increment" column in `requirements.md`, the version column in `traceability_matrix.md`, the tag table in `README.md`, and the version references in `ml_pipeline.md` and the prompt files, so every document uses the same numbers.
