"""
clean_weather.py
Clean and preprocess raw weather data:
- Convert temperature to Celsius (if needed)
- Parse date & time
- Handle missing data
- Aggregate daily statistics
"""

import os
import pandas as pd

# Compute root dir dynamically
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from scripts/

raw_file = os.path.join(ROOT_DIR, 'data', 'raw', 'weather_data.csv')
processed_dir = os.path.join(ROOT_DIR, 'data', 'processed')
os.makedirs(processed_dir, exist_ok=True)

# Load data
df = pd.read_csv(raw_file)
print(df.head())


# Parse datetime column
df['datetime'] = pd.to_datetime(df['datetime'])

# Handle missing data: drop rows with missing critical values
df.dropna(subset=['temperature_C', 'humidity'], inplace=True)

# Aggregate daily stats
df['date'] = df['datetime'].dt.date

daily_stats = df.groupby(['city', 'date']).agg({
    'temperature_C': ['mean', 'min', 'max'],
    'humidity': 'mean',
    'wind_speed': 'mean'
}).reset_index()

# Flatten multi-index columns
daily_stats.columns = [
    'city', 'date',
    'avg_temp_C', 'min_temp_C', 'max_temp_C',
    'avg_humidity', 'avg_wind_speed'
]

print("\n✅ Cleaned & aggregated data:")
print(daily_stats.head())

# Save cleaned/aggregated data
clean_file = os.path.join(processed_dir, 'clean_weather_data.csv')
daily_stats.to_csv(clean_file, index=False)

print(f"✅ Cleaned data saved to {clean_file}")
