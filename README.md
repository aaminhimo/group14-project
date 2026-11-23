# AI Energy Consumption Forecasting Dashboard

## 1. Group information

| | |
|---|---|
| Group | **14** |
| Case study | AI Energy Consumption Forecasting Dashboard |
| Course | CS13477 Software Engineering, Fall 2026 (PSUT) |
| Instructor | Dr. Samer El Kababji |

| Member | Student ID | Main responsibility |
|---|---|---|
| Mohammad Wadi | 20230719 | Data layer: ingestion, database, data API, ERD/DFD, data tests |
| Kareem Qasmiya | 20230035 | Frontend dashboard, use case descriptions, UI/system tests |
| Mohammad Harbieh | 20230440 | ML pipeline and prediction service, `ml_pipeline.md`, model tests |
| Amin Himo | 202301238 | Architecture/UML, documentation, traceability, repo admin, report |

## 2. Project overview

- **Purpose:** analyse building and environmental measurements and predict appliance energy use (Wh).
- **Expected final outcome:** web dashboard with historical data, predicted consumption, actual-vs-predicted comparison, what-if and simulated live predictions, alerts and reports.
- **Technology:** Python 3.11, FastAPI, SQLAlchemy/SQLite, pandas, scikit-learn, HTML/JS + Plotly.js, pytest; Mermaid for diagrams; Claude Code as the coding agent.
- **Dataset:** [UCI Appliances Energy Prediction](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) (CC BY 4.0), 19,735 rows at 10-minute steps.

## 3. Architecture and diagrams

| Diagram | Description |
|---|---|
| [Use case diagram and descriptions](docs/architecture/use_cases.md) | Actors and the seven use cases UC-01…UC-07 |
| [C4 L1: System Context](docs/architecture/c4_context.md) | Users, the dashboard, and the UCI data source |
| [C4 L2: Containers](docs/architecture/c4_container.md) | Web dashboard, backend API, ingestion job, training pipeline, SQLite DB, model store |
| [Sequence diagrams SD-01…05](docs/architecture/sequence_diagrams.md) | Ingest/train, history, what-if, compare, replay + alerts |
| [ERD](docs/architecture/data_model.md) | measurements, predictions, model_runs, replay_sessions, alerts |
| [Dataset analysis](docs/dataset/dataset_analysis.md) | Data quality, target distribution, daily profile, baselines |

Later diagrams (data flow, component, class, activity, state, deployment) are planned in the incremental plan.

## 4. Repository structure

| Folder | Contents |
|---|---|
| `docs/` | Requirements, architecture, plan, traceability, AI log; `docs/architecture/` (one page per diagram), `docs/dataset/` |
| `uml/` | Editable Mermaid sources and `rendered/` PNGs |
| `src/` | Application code (`backend/`, `ml/`, `frontend/`), built from v0.2.0 on |
| `tests/` | `unit/`, `component/`, `integration/`, `system/`, `ml/` |
| `data/` | Download instructions and a 432-row sample (full dataset not committed) |
| `prompts/` | One Markdown record per coding-agent task |
| `config/` | Example environment settings |

## 5. Incremental development

| Tag | Capability | Status |
|---|---|---|
| `v0.1.0-design` | Design baseline: requirements, use cases, C4 L1/L2, sequence diagrams, ERD, dataset analysis | Oral Exam 1 |
| `v0.1.0` | Project setup: folder layout, dependencies, config, environment check | Oral Exam 1 |
| `v0.2.0` | Data ingestion job | planned |
| `v0.3.0` | Measurements API | planned |
| `v0.4.0` | History dashboard | planned |
| `v0.5.0` | ML training pipeline | planned |
| `v0.6.0` | Prediction API | planned |
| `v0.7.0` | Actual vs predicted comparison | planned |
| `v0.8.0` | What-if and simulated live replay | planned |
| `v0.9.0` | Alerts and reporting | planned |
| `v1.0.0` | Final integrated release | planned |

Each capability has a `-design` tag before its working tag. Full plan: (https://github.com/aaminhimo/group14-project/blob/main/docs/incremental_development_plan%20(2).md)

## 6. Contributions

Commit counts from `git shortlog -sn --all --no-merges` (updated before each oral exam; count alone does not measure contribution quality).

| Member | Commits | Main contributions |
|---|---|---|
| Mohammad Wadi | 26 | |
| Kareem Qasmiya | 20 | |
| Mohammad Harbieh | 2 | |
| Amin Himo | 8 | |

---

### Run (from v0.1.0)

```bash
python -m venv .venv && .venv\Scripts\activate      # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/check_env.py
```

Download the dataset from the link in section 2 and place `energydata_complete.csv` in `data/raw/`. The automatic download and the web app come in v0.2.0 and later.
