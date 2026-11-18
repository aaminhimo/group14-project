# ML Pipeline

> Version: v0.1.0-design (draft; finalised at v0.2.0-design) · Owner: Member B · Evidence: [dataset/dataset_analysis.md](dataset/dataset_analysis.md)

The model is a **component** of the system (the ML Training Pipeline container plus the Model Artifact Store), not a notebook.

## 1. Dataset source and licence
UCI Appliances Energy Prediction (id 374), CC BY 4.0, accessed 2026-11-11, 19,735 rows × 29 columns. Download: `python data/download_data.py`.

## 2. Target variable
`Appliances`: energy used by household appliances in each 10-minute interval, in **Wh** (range 10–1080, median 60, mean 97.7).

## 3. Preprocessing pipeline (in order)
1. Parse `date` to a timestamp and sort ascending.
2. Validate: 29 columns, no nulls, unique timestamps (the dataset has 0 nulls and 0 duplicates; anything else is rejected at ingestion).
3. Drop `rv1`, `rv2` (identical random noise).
4. Derive time features: `hour`, `weekday`, `is_weekend`, plus cyclic `hour_sin`/`hour_cos`.
5. *(Next-step mode only)* derive lag features: `Appliances` at t−1, t−2, t−3 and a 6-step (1 h) rolling mean computed from past values only. Drop the first 6 rows, which have no history.
6. Optional: train on `log1p(Appliances)` to tame spikes; predictions are converted back with `expm1`.
7. Scale features only for models that need it (linear regression), inside a scikit-learn `Pipeline` so that the scaler is fitted on training data only.

## 4. Train / validation / test strategy
Chronological, never shuffled:

| Split | Share | Period |
|---|---|---|
| Train | 70% | 2016-01-11 17:00 → 2016-04-16 15:10 |
| Validation | 15% | 2016-04-16 15:20 → 2016-05-07 04:30 |
| Test | 15% | 2016-05-07 04:40 → 2016-05-27 18:00 |

Model selection and tuning use validation only. The test set is scored **once** for the final report.

## 5. Models and evaluation metrics

| Mode | Inputs | Candidates | Must beat |
|---|---|---|---|
| What-if (conditions) | conditions + time features | LinearRegression, RandomForest, GradientBoosting | mean baseline (test MAE 52.8) |
| Next-step forecast | conditions + time + lag features | same | persistence (test MAE 26.7, RMSE 66.8, R² 0.46) |

Metrics: **MAE** (typical error in Wh), **RMSE** (penalises spikes), **R²** (share of variance explained). Appliance energy is noisy and spiky, so modest R² is expected and will be reported honestly.

## 6. How predictions reach the software
- Training saves `models/energy_model.joblib` (a dict with the fitted pipelines for both modes, the feature lists and the version string) and `models/metrics.json`, and inserts a row in `model_runs`.
- The Backend API loads the artifact **once at startup** (`src/ml/model_store.py`), exposes it via `POST /api/predict` (what-if) and internally in compare and replay, and stores every prediction in `predictions`.
- If the artifact is missing, prediction endpoints return 503 while the history endpoints keep working.

## Block diagram (for the oral exam)

```
conditions + time (+ recent readings) ──► preprocessing ──► trained model ──► predicted Wh
                                                                    │
                       Backend API (/predict, /compare, /replay) ◄──┘──► Web Dashboard (next to actual values)
```
