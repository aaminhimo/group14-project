# Traceability Matrix

> Updated at every tag. Status values: *Designed* → *Implemented* → *Passing* (or *Failing* with a note).

| Requirement ID | Use Case / Design Element | Increment / Version | Implementation Module(s) | Test(s) | Status |
|---|---|---|---|---|---|
| FR-01 | UC-01; SD-01; ERD `measurements` | v0.1.0 | `src/backend/ingest/download.py`, `src/backend/ingest/loader.py` | `tests/unit/test_loader_validation.py`, `tests/integration/test_ingest.py` | Designed |
| FR-02 | UC-03; SD-02 | v0.1.0 | `src/backend/app/api/measurements.py`, `services/measurement_service.py` | `tests/integration/test_measurements_api.py` | Designed |
| FR-03 | UC-03; SD-02 | v0.1.0 | `src/frontend/js/history.js` | `tests/system/test_history_page.py` | Designed |
| FR-04 | UC-03; SD-02 | v0.1.0 | `services/measurement_service.py` (summary), `src/frontend/js/history.js` | `tests/unit/test_summary_stats.py` | Designed |
| FR-05 | UC-02; SD-01 | v0.2.0 | `src/ml/features.py` | `tests/unit/test_features.py` | Designed |
| FR-06 | UC-02; SD-01; ERD `model_runs` | v0.2.0 | `src/ml/train.py`, `src/ml/evaluate.py`, `src/ml/model_store.py` | `tests/ml/test_model_quality.py` | Designed |
| FR-07 | UC-05; SD-03 | v0.3.0 | `src/backend/app/api/predictions.py`, `services/prediction_service.py` | `tests/component/test_prediction_service.py`, `tests/integration/test_predict_api.py` | Designed |
| FR-08 | UC-05; SD-03; ERD `predictions` | v0.3.0 | `services/prediction_service.py`, `models.py` | `tests/integration/test_predict_api.py` | Designed |
| FR-09 | UC-04; SD-04 | v0.4.0 | `src/backend/app/api/compare.py`, `src/frontend/js/compare.js` | `tests/system/test_compare_page.py` | Designed |
| FR-10 | UC-04; SD-04 | v0.4.0 | `services/comparison_service.py`, `src/ml/evaluate.py` | `tests/unit/test_metrics.py` | Designed |
| FR-11 | UC-05; SD-03 | v0.5.0 | `src/frontend/js/whatif.js` | `tests/system/test_whatif_flow.py` | Designed |
| FR-12 | UC-06; SD-05; ERD `replay_sessions` | v0.5.0 | `src/backend/app/api/replay.py`, `services/replay_service.py` | `tests/integration/test_replay_api.py` | Designed |
| FR-13 | UC-06; SD-05 | v0.5.0 | `services/replay_service.py`, `services/prediction_service.py` | `tests/integration/test_replay_api.py` | Designed |
| FR-14 | UC-07; SD-05; ERD `alerts` | v0.6.0 | `services/alert_service.py` | `tests/unit/test_alert_rules.py` | Designed |
| FR-15 | UC-07 | v0.6.0 | `src/backend/app/api/alerts.py` | `tests/integration/test_alerts_api.py` | Designed |
| FR-16 | UC-07 | v0.6.0 | `src/backend/app/api/reports.py`, `services/report_service.py` | `tests/integration/test_reports_api.py` | Designed |
| NFR-03 | SD-03 error paths | v0.3.0 | `api/predictions.py` | `tests/integration/test_predict_api.py` | Designed |
| NFR-04 | ml_pipeline §5 | v0.2.0 | `src/ml/evaluate.py` | `tests/ml/test_model_quality.py` | Designed |
