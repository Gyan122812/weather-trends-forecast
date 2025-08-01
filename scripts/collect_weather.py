# """
# collect_weather.py
# Fetch real-time weather data for selected cities using OpenWeatherMap API
# and save to CSV in data/raw/
# """

# import requests
# import pandas as pd
# from datetime import datetime
# import os

# # Configuration
# API_KEY = '3ce86f958717050d0fd11b92d47bbfd2'
# CITIES = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# # Function to fetch weather data for a single city
# def fetch_weather(city):
#     params = {'q': city, 'appid': API_KEY}
#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     print(f"\n📦 Raw response for {city}: {data}\n")

#     if response.status_code != 200:
#         raise Exception(f"API call failed for {city}: {data.get('message', 'Unknown error')}")

#     # Parse data
#     weather_info = {
#         'city': city,
#         'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#         'temperature_C': round(data['main']['temp'] - 273.15, 2),
#         'humidity': data['main']['humidity'],
#         'weather': data['weather'][0]['description'],
#         'wind_speed': data['wind']['speed']
#     }
#     return weather_info

# # Fetch data for all cities
# all_weather_data = []

# for city in CITIES:
#     try:
#         print(f'Fetching weather data for {city}...')
#         weather = fetch_weather(city)
#         all_weather_data.append(weather)
#         print(f"✅ Parsed weather data for {city}: {weather}")

#     except Exception as e:
#         print(f"Error fetching data for {city}: {e}")

# # Convert to DataFrame
# df = pd.DataFrame(all_weather_data)


# # Always save to data/raw under project root
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
# output_dir = os.path.join(PROJECT_ROOT, 'data', 'raw')
# os.makedirs(output_dir, exist_ok=True)

# csv_file = os.path.join(output_dir, 'weather_data.csv')

# print("\n📊 DataFrame to be saved:")
# print(df)
# df.to_csv(csv_file, index=False)

# print(f"✅ Weather data saved to {csv_file}")






"""
collect_weather.py
Fetch real-time weather data for selected cities using OpenWeatherMap API
and append to CSV in data/raw/ to keep historical data.
"""

import requests
import pandas as pd
from datetime import datetime
import os

# Configuration
API_KEY = '3ce86f958717050d0fd11b92d47bbfd2'
CITIES = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Compute output file path dynamically (always under data/raw)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
output_dir = os.path.join(PROJECT_ROOT, 'data', 'raw')
os.makedirs(output_dir, exist_ok=True)
csv_file = os.path.join(output_dir, 'weather_data.csv')

# Function to fetch weather data for a single city
def fetch_weather(city):
    params = {'q': city, 'appid': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(f"\n📦 Raw response for {city}: {data}\n")

    if response.status_code != 200:
        raise Exception(f"API call failed for {city}: {data.get('message', 'Unknown error')}")

    # Parse data
    weather_info = {
        'city': city,
        'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature_C': round(data['main']['temp'] - 273.15, 2),
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed']
    }
    return weather_info

# Fetch data for all cities
all_weather_data = []
for city in CITIES:
    try:
        print(f'Fetching weather data for {city}...')
        weather = fetch_weather(city)
        all_weather_data.append(weather)
        print(f"✅ Parsed weather data for {city}: {weather}")
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")

# Convert new data to DataFrame
df_new = pd.DataFrame(all_weather_data)
print("\n📊 New data collected:")
print(df_new)

# Append mode: if old data exists, load and merge
if os.path.exists(csv_file):
    df_old = pd.read_csv(csv_file)
    df_combined = pd.concat([df_old, df_new], ignore_index=True)
else:
    df_combined = df_new

# Save combined data
df_combined.to_csv(csv_file, index=False)
print(f"\n✅ Weather data saved to {csv_file}")


