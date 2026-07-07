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