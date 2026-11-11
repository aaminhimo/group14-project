# Data

The full dataset (12 MB) is **not committed** (instructor rule §7, NFR-07).

| File | Committed | How to get it |
|---|---|---|
| `raw/energydata_complete.csv` | No (git-ignored) | `python -m src.backend.ingest.download` |
| `sample/energydata_sample.csv` | Yes | First 432 rows (3 days, 2016-01-11 17:00 → 2016-01-14 16:50); used by tests |
| `energy.db` | No (git-ignored) | Created by the ingestion job |

Source: UCI Appliances Energy Prediction, CC BY 4.0. Cite Candanedo et al., *Energy and Buildings* 140 (2017). Analysis: [docs/dataset/dataset_analysis.md](../docs/dataset/dataset_analysis.md).
