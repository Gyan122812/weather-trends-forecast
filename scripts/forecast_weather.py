"""
forecast_weather.py
Forecast daily average temperature using Prophet.
"""

import os
import pandas as pd
from prophet import Prophet

# Step 1: Compute root dir dynamically (just like before)
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Step 2: Load cleaned data
clean_file = os.path.join(ROOT_DIR, 'data', 'processed', 'clean_weather_data.csv')
df = pd.read_csv(clean_file)
print("✅ Cleaned data loaded:")
print(df.head())

# Step 3: Filter for one city (example: Delhi)
city = 'Delhi'
city_df = df[df['city'] == city].copy()

# Step 4: Prepare data for Prophet
# Prophet needs columns: 'ds' (date), 'y' (value to forecast)
city_df.rename(columns={'date': 'ds', 'avg_temp_C': 'y'}, inplace=True)
city_df['ds'] = pd.to_datetime(city_df['ds'])

# Step 5: Fit Prophet model
model = Prophet()
print("\n📊 Data passed to Prophet:")
print(city_df[['ds', 'y']])
model.fit(city_df[['ds', 'y']])

# Step 6: Create future dataframe (e.g., next 7 days)
future = model.make_future_dataframe(periods=7)

# Step 7: Predict
forecast = model.predict(future)

# Show forecast
print("\n✅ Forecasted data:")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# Step 8: Save forecast to CSV
forecast_dir = os.path.join(ROOT_DIR, 'data', 'forecast')
os.makedirs(forecast_dir, exist_ok=True)

forecast_file = os.path.join(forecast_dir, f'{city}_temperature_forecast.csv')
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(forecast_file, index=False)

print(f"\n✅ Forecast saved to {forecast_file}")

