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
| Mohammad Wadi | 20230719 | //Data layer: ingestion, database, data API, ERD/DFD, data tests |
| Kareem Qasmiya | 20230035 | //Frontend dashboard, use case descriptions, UI/system tests |
| Mohammad Harbieh | 20230440 | //ML pipeline and prediction service, `ml_pipeline.md`, model tests |
| Amin Himo | 202301238 | //Architecture/UML, documentation, traceability, repo admin, report |

## 2. Project overview

- **Purpose:** analyse building and environmental measurements and predict appliance energy use (Wh).
- **Expected final outcome:** web dashboard with historical data, predicted consumption, actual-vs-predicted comparison, what-if and simulated live predictions, alerts and reports.
- **Technology:** Python 3.11, FastAPI, SQLAlchemy/SQLite, pandas, scikit-learn, HTML/JS + Plotly.js, pytest; Mermaid for diagrams; Claude Code as the coding agent.
- **Dataset:** [UCI Appliances Energy Prediction](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) (CC BY 4.0), 19,735 rows at 10-minute steps.

## 3. Architecture and diagrams

| Diagram | Description |
|---|---|
| [C4 L1: System Context](docs/architecture/c4_context.md) | Users, the dashboard, and the UCI data source |
| [C4 L2: Containers](docs/architecture/c4_container.md) | Web dashboard, backend API, ingestion job, training pipeline, SQLite DB, model store |
| [Sequence diagrams SD-01…05](docs/architecture/sequence_diagrams.md) | Container-level flows: ingest/train, history, what-if, compare, replay + alerts |
| [ERD](docs/architecture/data_model.md) | measurements, predictions, model_runs, replay_sessions, alerts |
| [Dataset analysis](docs/dataset/dataset_analysis.md) | Data quality, target distribution, daily profile, baselines |

## 4. Repository structure

| Folder | Contents |
|---|---|
| `docs/` | Mandatory documents; `docs/architecture/` (one page per diagram), `docs/dataset/` |
| `uml/` | Editable Mermaid sources (`c4/`, `sequence/`, `data/`, `charts/`) and `rendered/` PNGs |
| `src/` | `backend/` (FastAPI app + ingestion), `ml/` (training), `frontend/` (dashboard) |
| `tests/` | `unit/`, `component/`, `integration/`, `system/`, `ml/` |
| `data/` | Download instructions and a 432-row sample (full dataset not committed) |
| `prompts/` | One Markdown record per coding-agent task |
| `config/` | Example environment settings |
| `tools/` | Diagram rendering script |

## 5. Incremental development

| Tag | Capability |
|---|---|
| `v0.1.0-design` | Architecture baseline: requirements, C4 L1/L2, sequence diagrams, ERD, dataset analysis, code skeleton |
| `v0.1.0` | _planned:_ data ingestion + historical dashboard |
| `v0.2.0` | _planned:_ ML training pipeline |
| `v0.3.0` | _planned:_ prediction API |
| `v0.4.0` | _planned:_ actual vs predicted comparison |
| `v0.5.0` | _planned:_ what-if + simulated live replay |
| `v0.6.0` | _planned:_ alerts + reporting |
| `v1.0.0` | _planned:_ final integrated release |

Full plan: [docs/incremental_development_plan.md](docs/incremental_development_plan.md)

## 6. Contributions

Commit counts from `git shortlog -sn --all --no-merges` (updated before each oral exam; count alone does not measure contribution quality).

| Member | Commits | Main contributions |
|---|---|---|
| _to be filled_ | | |

---

### Run (from v0.1.0 on)

```bash
python -m venv .venv && .venv\Scripts\activate      # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m src.backend.ingest.download
uvicorn src.backend.app.main:app --reload            # open http://127.0.0.1:8000
```

Re-render diagrams after editing a `.mmd` file: `npm install` (once), then `npm run diagrams`.
