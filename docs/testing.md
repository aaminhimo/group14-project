# Testing Strategy

| Level | What it checks here | Example | Folder |
|---|---|---|---|
| Unit | One function in isolation | schema validation rejects a 28-column CSV; `hour` feature derived correctly; MAE function | `tests/unit` |
| Component | One module with dependencies stubbed | `PredictionService` with a fake model returns a float in Wh | `tests/component` |
| Integration | Modules together (real SQLite test DB, real artifact) | `/api/measurements` returns the sample rows; `/api/predict` returns 422 on bad input | `tests/integration` |
| System / E2E | User flow through the running app | open dashboard, pick dates, chart has data; submit what-if, see prediction | `tests/system` |
| Model evaluation | ML quality, not code correctness | test MAE beats persistence / mean baselines | `tests/ml` |

**Rules.** Every working tag ships with its own tests passing. The test run output is saved to `docs/test_reports/<version>.md`. Failing or flaky tests are explained, never deleted. Tests use `data/sample/energydata_sample.csv`, so they do not need the full download.

**Run:** `pytest -q` (all) · `pytest tests/unit -q` (one level).

## Test reports
- v0.1.0-design: design checkpoint, no executable tests yet.
