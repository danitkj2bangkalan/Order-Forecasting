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
| 5  | Task3.ipynb                        | Explore Analysis in order to find insight from weekly_features_2024_2025.csv                  |
| 6  | main_source.py                     | this file contain several function that call in Task1.ipynb                                   |

## What delivered

in Task 1 and Task 2 i propose NeuralProphet model, this model has capabilities such as Hybrid Architecture, Autoregressive Neural Network (AR-Net) Integration.
NeuralProphet allows for deep customization, Scalable Engine and GLobal Modeling, faster than previous model(Facebook Prophet) and often beats Prophet for short-term forecasts because of its auto-regressive (AR) components 
NeuralProphet breaks down forecasts into simple parts like trend and seasonality, works great on both small and large datasets and handles complex seasonal patterns better.

### Task 1

This section captured seasonality by (trend, season_daily, season_weekly, season_yearly and also holiday in indonesia), i structure data use pandas accross 10 merchant first before fit to model and also backtesting shceme by splitting data 80% and 20% then predict for 2026-01-01 → 2026-06-30

### Task 2

This section captured seasonality every merchant by (trend, season_daily, season_weekly, season_yearly) and modify dataset only use date,order_count and rename company to ID because in neuralprophet can distinguish each distinct time series entity then spilt dataset by False value in local_split before evaluate model

### Task 3

This section explored what find insight from weekly_features_2024_2025.csv such as Time-Series & Seasonality Analysis, Comparative & Categorical Analysis, Ratio & Efficiancy Analysis, Marketplace Composition Analysis, Correlation & Multivariate Analysis, Outlier & Anomaly Detection and prediction intervals / uncertainty with defined two quantiles, 0.1 and 0.9, which correspond to the 10th and 90th percentiles of the distribution of the forecast 

## Note for Code

if you want to run Task1.ipynb,Task2.ipynb,Task3.ipynb and main.py dont forget to install necessary library such as numpy,pandas,neuralprophet,matplotlib,seaborn then running inside of virtual environment in python

if you want to run Task1.ipynb inside virtual environment python dont forget to downgrade pandas version when installing pip,This brings back the deprecated attribute and lets NeuralProphet run smoothly.

    FutureWarning: Series.view is deprecated and will be removed in a future version. Use ``astype`` as an alternative to change the dtype.
    converted_ds = pd.to_datetime(ds_col, utc=True).view(dtype=np.int64)

    >>pip install "pandas<3.0.0" 

if you want to run Task2.ipynb inside virtual environment python Downgrade PyTorch if run task2 because weight_only defaults to False
    >>pip install torch==2.5.1
because torch in neuralprophet support global modeling in torch==2.5.1 version 