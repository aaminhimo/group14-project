# Requirements

> Version: v0.1.0-design · IDs are stable: never renumber; mark removed ones as *withdrawn*.

## Use cases

| ID | Use case | Primary actor | Requirements |
|---|---|---|---|
| UC-01 | Ingest dataset | Data Scientist | FR-01 |
| UC-02 | Train and evaluate model | Data Scientist | FR-05, FR-06 |
| UC-03 | View historical measurements | Energy Analyst | FR-02, FR-03, FR-04 |
| UC-04 | Compare actual vs predicted | Energy Analyst | FR-09, FR-10 |
| UC-05 | Run what-if prediction | Building Manager | FR-07, FR-08, FR-11 |
| UC-06 | Run simulated live replay | Building Manager | FR-12, FR-13 |
| UC-07 | Review alerts and report | Building Manager | FR-14, FR-15, FR-16 |

## Functional requirements

| ID | Requirement | Priority | Increment |
|---|---|---|---|
| FR-01 | The system shall download the dataset, validate its schema (29 expected columns, parseable timestamps, no duplicates) and load all valid rows into the database; re-running shall not create duplicates. | Must | v0.1.0 |
| FR-02 | The system shall return measurements for a user-selected date range and set of variables. | Must | v0.1.0 |
| FR-03 | The dashboard shall chart appliance and lights energy over the selected range. | Must | v0.1.0 |
| FR-04 | The dashboard shall chart indoor/outdoor temperature and humidity and show min/mean/max summaries. | Must | v0.1.0 |
| FR-05 | The training pipeline shall derive time features (hour, weekday, weekend) and lag features, and split data chronologically 70/15/15. | Must | v0.2.0 |
| FR-06 | The pipeline shall train baselines (mean, persistence) and at least two models, report MAE/RMSE/R², and save the chosen model with its metrics and version. | Must | v0.2.0 |
| FR-07 | The API shall accept a set of conditions, validate it and return predicted appliance energy in Wh with the model version. | Must | v0.3.0 |
| FR-08 | Every prediction shall be stored with its inputs, source and model version, and be retrievable. | Must | v0.3.0 |
| FR-09 | The dashboard shall overlay actual and predicted energy for a selected period. | Must | v0.4.0 |
| FR-10 | The system shall compute MAE, RMSE and R² for the selected period. | Must | v0.4.0 |
| FR-11 | The dashboard shall provide a what-if form pre-filled with typical values and display the prediction. | Must | v0.5.0 |
| FR-12 | The system shall replay historical readings as a simulated live stream at a configurable speed, with start, pause and stop. | Must | v0.5.0 |
| FR-13 | During replay, the system shall predict the next-step energy for each reading and update the live chart. | Should | v0.5.0 |
| FR-14 | The system shall raise an alert when predicted or actual energy exceeds a configurable threshold (default 400 Wh). | Must | v0.6.0 |
| FR-15 | The system shall keep an alert log viewable on the dashboard. | Must | v0.6.0 |
| FR-16 | The system shall produce a summary report (trends, error metrics, alerts) for a period, exportable as CSV. | Should | v0.6.0 |

## Non-functional requirements

| ID | Category | Requirement | Verification |
|---|---|---|---|
| NFR-01 | Performance | A history query for one month returns in < 2 s on a laptop; charts downsample above 5,000 points. | Integration test with timing |
| NFR-02 | Performance | A single `/api/predict` call returns in < 500 ms (model cached in memory). | Integration test |
| NFR-03 | Reliability | Invalid input returns HTTP 422 with field errors; a missing model returns 503; the API never crashes on bad input. | API tests |
| NFR-04 | ML quality | The next-step model beats persistence and the what-if model beats the mean baseline on the test set (MAE). | `tests/ml` + metrics report |
| NFR-05 | Maintainability | Code is layered (api / services / models) and every working increment ships with passing automated tests. | Code review, CI run |
| NFR-06 | Portability | Runs from README instructions on a clean Windows/macOS/Linux machine with Python 3.11+. | Clean-machine run before v1.0.0 |
| NFR-07 | Data governance | The full dataset and secrets are never committed; the dataset licence (CC BY 4.0) is credited. | PR checklist |
| NFR-08 | Traceability | Each requirement maps to design, code and tests in `docs/traceability_matrix.md`. | Review at each tag |
