from sklearn.linear_model import LinearRegression
import streamlit as st
import pandas as pd
import numpy as np
from database_connection import import_weight_database
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from matplotlib import rc

class DataFrame:
    def _forecast(self, series, periods):
        """ Linear Regression Forecasting"""
        X = np.arange(len(series)).reshape(-1, 1)
        y = series.values
        model = LinearRegression()
        model.fit(X, y)
        forecast = model.predict(np.arange(len(series), len(series) + periods).reshape(-1, 1))
        return forecast

    def _new_dataframe(self, weight_df):
        """ Predict the weight for the next 60 days """
        forecasts =  {}
        forecast_period = 60
        for column in weight_df.columns:
            # Iterate over each column of the dataframe {weight, mf, muscle} and make predictions for the next 60 days; store them into a dictionary
            forecasts[column] = self._forecast(weight_df[column], forecast_period)
            
        # Create a series of dates, which starts from the next day of the last day of the actual weight mesurements + 60 days
        forecast_dates = pd.date_range(start = weight_df.index[-1] + pd.Timedelta(days=1), periods=forecast_period)
        
        # Create a dataframe of forecasts
        forecast = pd.DataFrame(forecasts, index = forecast_dates)
        
        # Add the last_row of the measurements as a first row of predictions, not to create gaps in the plot
        forecast = pd.concat([weight_df.iloc[-1:], forecast], ignore_index = False)
        
        return forecast
    
    def __init__(self):
        # Import the weight dataframe and preprocess it
        self.weightdataframe = import_weight_database()
        self.weightdataframe['data'] = pd.to_datetime(self.weightdataframe['data'], format='%d/%m/%Y')
        self.weightdataframe.set_index('data', inplace=True)
        self.forecastedf = self._new_dataframe(self.weightdataframe)

def make_plot(measurements, predictions):
    # Create a double-axis figure
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces, one for each value {weight, bodyfat, and muscle}, both measurements and predictions
    fig.add_trace(go.Scatter(x=measurements.index, y=measurements['peso'], name="Weight", mode = 'lines'), secondary_y=False)
    fig.add_trace(go.Scatter(x=predictions.index, y=predictions['peso'], name="Predicted Weight", opacity = 0.7), secondary_y=False)

    fig.add_trace(go.Scatter(x=measurements.index, y=measurements['bodyfat'], name="BodyFat%", mode = 'lines'), secondary_y=True)
    fig.add_trace(go.Scatter(x=predictions.index, y=predictions['bodyfat'], name="Predicted BodyFat%", opacity = 0.7), secondary_y=True)

    fig.add_trace(go.Scatter(x=measurements.index, y=measurements['muscle'], name="Muscle%", mode = 'lines'), secondary_y=True)
    fig.add_trace(go.Scatter(x=predictions.index, y=predictions['muscle'], name="Predicted Muscle%", opacity = 0.7), secondary_y=True)

    # Add title
    fig.update_layout(title_text="Weight, Bodyfat and Daily Trend", legend_orientation='h')

    # Set x-axis title
    fig.update_xaxes(fixedrange = True)

    # Set y-axes title
    fig.update_yaxes(title_text="Weight in kilograms", secondary_y=False, showgrid = True, fixedrange = True)
    fig.update_yaxes(title_text="Bodyfat and Muscle in %", secondary_y=True, showgrid = False, fixedrange = True)
    
    st.plotly_chart(fig, theme = 'streamlit', use_container_width = True, config={'displayModeBar': False, 'editable': False})
    
st.set_page_config(layout = 'wide')
st.title("Weight, Bodyfat, and Muscle Daily Measurements and Trends")
data = DataFrame()

measurements = data.weightdataframe
predictions = data.forecastedf

st.dataframe(measurements.style.format({
    'peso': '{} kg'.format,
    'bodyfat': '{:,.2%}'.format,
    'muscle': '{:,.2%}'.format,
}), use_container_width = True)

make_plot(measurements, predictions)