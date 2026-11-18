# Project Description

> CS13477 Software Engineering · Fall 2026 · **Group 14** · Case study: **AI Energy Consumption Forecasting Dashboard**

## Problem

Building operators collect temperature, humidity, weather and energy readings but cannot easily see how appliance energy use relates to conditions, or what consumption to expect next. This project builds a software system that analyses building and environmental measurements and **predicts appliance energy use**. It integrates data ingestion, forecasting/regression, visualisation and what-if/simulated readings into one coherent web dashboard.

## Expected final outcome (from the case study)

A functional **web dashboard** showing:

1. historical energy and environmental measurements;
2. predicted consumption;
3. comparison of predictions with actual values;
4. predictions from simulated new input (what-if and replayed "live" readings);
5. high-consumption alerts and an integrated report (our extension of "integrated reporting").

## Stakeholders

| Stakeholder | Interest |
|---|---|
| Energy Analyst | Understand consumption patterns; judge prediction quality |
| Building Manager | Anticipate high consumption; test scenarios; get alerts and reports |
| Data Scientist (team) | Train, evaluate and replace the model safely |
| Instructor | Evidence of a disciplined, traceable, incremental SE process |

## Scope

**In scope:** single building (the dataset's house), historical data Jan–May 2016, one active model version, local deployment.
**Out of scope:** real sensors, multiple buildings, user accounts/roles, email/SMS notifications, cloud deployment.

## Assumptions

| ID | Assumption |
|---|---|
| A-01 | All data is historical. "Current readings" are **simulated by replaying** the dataset; there is no hardware. |
| A-02 | Users are anonymous or use one demo identity. No personal data exists. |
| A-03 | "Forecasting" means predicting `Appliances` (Wh per 10 min) from measured conditions (what-if), and the **next 10-minute step** from recent readings (replay). |
| A-04 | The full dataset is not committed. A download script and a 432-row sample are. |
| A-05 | The system runs locally (`uvicorn`) on Windows, macOS or Linux with Python 3.11+. |

## Dataset

UCI Appliances Energy Prediction: 19,735 rows × 29 columns, 10-minute steps, no missing values. Full analysis: [dataset/dataset_analysis.md](dataset/dataset_analysis.md).
