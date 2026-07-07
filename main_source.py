import pandas as pd
from neuralprophet import NeuralProphet, set_log_level

def rename_columns(df):
    df['canceled_count'] = df['company']
    df = df.rename(columns={'date': 'ds', 'order_count': 'y', 'canceled_count': 'ID'})
    df = df.drop(df.columns[0], axis=1)
    return df

def restructure_data(df):
    
    total_order = df.groupby('date')[['order_count', 'canceled_count']].sum().reset_index()
    total_order['y'] = total_order['order_count'] + total_order['canceled_count']
    total_order = total_order[['date', 'y']].rename(columns={'date': 'ds'})
    return total_order

set_log_level("ERROR")
def model():
    model = NeuralProphet(
            # n_lags=1,  # Autogression
            n_changepoints=0,
            # change_points_range=0.9,
            trend_reg=1.0, # Regularization for trend
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=True,
            # trend_reg=0.1, # Regularization for trend
            # seasonality_reg=0.1, # Regularization for seasonality
            learning_rate=0.1, # Learning rate for optimization
            epochs=500, # Number of epochs for training 
            )
    model.add_country_holidays(country_name='ID') # Add country holidays
    model.set_plotting_backend("plotly") # Set plotting backend to plotly
    return model

def split_data(model, df, valid_p=0.2):
    
    df_train, df_val = model.split_df(df, valid_p=valid_p)
    return df_train, df_val