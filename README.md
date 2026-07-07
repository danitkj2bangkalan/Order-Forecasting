# Order-Forecasting
Forecast their daily order volume for the first half of 2026. We have the actual 2026 numbers withheld and will score your forecast against Merchants ("companies") sell across marketplaces (Shopee, Tokopedia, Lazada, and others) — so this is a genuine test of whether your model generalizes, not just fits history.

## The Data

There are 6 in this repository:

| NO | File                               | Usage                                                                                         |
| -- | --------                           | ----------------------------------------------------------------------------------------------|
| 1  | daily_orders_2024_2025.csv         | This file used in Task 1 and Task 2                                                           |
| 2  | weekly_features_2024_2025.csv      | This file used in Task 3                                                                      |
| 3  | Task1.ipynb                        | Forecast total daily order volume across all 10 merchants combined for 2026-01-01 → 2026-06-30|
| 4  | Task2.ipynb                        | Forecast daily order volume for each of the 10 merchants individually for the same horizon.   |
| 5  | Task5.ipynb                        | Explore Analysis in order to find insight from weekly_features_2024_2025.csv                  |
| 6  | main_source.py                     | this file contain several function that call in Task1.ipynb                                   |

## What i delivered

in Task 1 and Task 2 i propose NeuralProphet model 

### Task 1

This section captured seasonality by (trend, season_daily, season_weekly, season_yearly and also holiday in indonesia), i structure data use pandas accross 10 merchant first before fit to model and also backtesting shceme by splitting data 80% and 20% then predict for 2026-01-01 → 2026-06-30

### Task 2

This section captured seasonality every merchant by (trend, season_daily, season_weekly, season_yearly) and modify dataset only use date,order_count and rename company to ID because in neuralprophet can distinguish each distinct time series entity then spilt dataset by False value in local_split before evaluate model

### Task 3

This section explored what find insight from weekly_features_2024_2025.csv such as Time-Series & Seasonality Analysis, Comparative & Categorical Analysis, Ratio & Efficiancy Analysis, Marketplace Composition Analysis, Correlation & Multivariate Analysis, Outlier & Anomaly Detection  