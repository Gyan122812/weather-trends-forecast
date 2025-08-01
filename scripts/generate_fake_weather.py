"""
generate_fake_weather.py
Create fake historical weather data for testing the forecast script.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Compute project root dynamically
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

# Output file in data/raw
output_dir = os.path.join(ROOT_DIR, 'data', 'raw')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'weather_data.csv')

# Cities to generate data for
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']

# Generate data for last 30 days
num_days = 30
today = datetime.today()

records = []

for city in cities:
    for i in range(num_days):
        date = today - timedelta(days=i)
        temperature = np.random.normal(loc=30, scale=5)  # average around 30°C
        humidity = np.random.randint(40, 90)
        wind_speed = np.random.uniform(1, 10)
        weather_desc = np.random.choice(['clear sky', 'overcast clouds', 'light rain', 'scattered clouds'])

        record = {
            'city': city,
            'datetime': date.strftime('%Y-%m-%d %H:%M:%S'),
            'temperature_C': round(temperature, 2),
            'humidity': humidity,
            'weather': weather_desc,
            'wind_speed': round(wind_speed, 2)
        }
        records.append(record)

# Create DataFrame
df = pd.DataFrame(records)

# Save to CSV
df.to_csv(output_file, index=False)

print(f"✅ Fake historical weather data generated and saved to: {output_file}")
print(df.head())
