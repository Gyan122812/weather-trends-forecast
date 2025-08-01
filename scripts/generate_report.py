"""
visualize_weather.py
Visualize weather trends using Matplotlib & Seaborn
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Always use a clean Seaborn style
sns.set(style='whitegrid')

# Paths
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))  # go up from scripts/
clean_file = os.path.join(ROOT_DIR, 'data', 'processed', 'clean_weather_data.csv')
figures_dir = os.path.join(ROOT_DIR, 'reports', 'figures')
os.makedirs(figures_dir, exist_ok=True)

# Load data
df = pd.read_csv(clean_file)
print("✅ Cleaned data loaded:")
print(df.head())

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Plot 1: Daily Average Temperature per City
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='avg_temp_C', hue='city', marker='o')
plt.title('Daily Average Temperature per City')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
temp_plot_file = os.path.join(figures_dir, 'avg_temperature_trend.png')
plt.savefig(temp_plot_file)
plt.close()
print(f"✅ Saved: {temp_plot_file}")

# Plot 2: Daily Average Humidity per City
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='avg_humidity', hue='city', marker='o')
plt.title('Daily Average Humidity per City')
plt.xlabel('Date')
plt.ylabel('Average Humidity (%)')
plt.xticks(rotation=45)
plt.tight_layout()
humidity_plot_file = os.path.join(figures_dir, 'avg_humidity_trend.png')
plt.savefig(humidity_plot_file)
plt.close()
print(f"✅ Saved: {humidity_plot_file}")

# Plot 3: Daily Average Wind Speed per City
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='avg_wind_speed', hue='city', marker='o')
plt.title('Daily Average Wind Speed per City')
plt.xlabel('Date')
plt.ylabel('Average Wind Speed (m/s)')
plt.xticks(rotation=45)
plt.tight_layout()
wind_plot_file = os.path.join(figures_dir, 'avg_wind_speed_trend.png')
plt.savefig(wind_plot_file)
plt.close()
print(f"✅ Saved: {wind_plot_file}")

print("✅ All plots created and saved in reports/figures/")
