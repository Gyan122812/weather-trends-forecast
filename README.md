# 🌦️ Real-Time Weather Trends & Forecast

Analyze real-time weather data for major Indian cities using OpenWeatherMap API.  
Forecast temperature trends, visualize seasonal patterns, compare cities, and auto-generate HTML reports — all with Python.

---

## 📌 **Project Goal**
- Collect & clean real-time weather data for Indian cities
- Forecast future temperature trends using Prophet
- Visualize weather trends (temperature, humidity, wind speed)
- Auto-generate an HTML report for easy sharing

---

## 🗂 **Dataset**
- Source: [OpenWeatherMap API](https://openweathermap.org/)
- Cities: Delhi, Mumbai, Bangalore, Chennai, Kolkata

---

## 🛠 **Tools & Libraries**
- Python: `requests`, `pandas`, `prophet`, `matplotlib`, `seaborn`, `jinja2`
- SQLite (optional for storage)

---

## ✨ **Key Features**
✅ Fetch real-time weather data via API  
✅ Clean & preprocess daily weather data  
✅ Time-series forecasting with Prophet  
✅ Visualize trends & save plots automatically  
✅ Auto-generate HTML report using Jinja2 templates

---

## 📊 **Project Outputs**
- CSV files with raw & processed weather data (`data/`)
- Forecast CSV files for selected cities (`data/forecast/`)
- Visual plots (PNG) saved in `reports/figures/`
- HTML report: `reports/weather_report.html`

---

## 📁 Folder Structure

```plaintext
weather-trends-forecast/
├── data/
│   ├── raw/                  # Raw data fetched from OpenWeatherMap API
│   ├── processed/            # Cleaned & transformed data
│   └── forecast/             # Forecasted CSV files (e.g., Delhi_temperature_forecast.csv)
├── reports/
│   ├── figures/              # Plots: temperature trends, humidity trends, wind speed trends
│   └── weather_report.html   # Auto-generated HTML report
├── scripts/                  # Python scripts for ETL, forecasting & reporting
│   ├── collect_weather.py        # Fetch real-time weather data
│   ├── clean_weather_data.py     # Clean and preprocess data
│   ├── forecast_weather.py      # Forecast temperatures with Prophet
│   ├── visualize_weather.py     # Create trend plots
│   └── generate_report.py       # Generate HTML report with plots & forecast
├── README.md                 # Project overview & instructions
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── .gitignore               # Ignore venv, __pycache__, etc.
```

---

## 🚀 **How to Run**
Clone the repository, install dependencies and run step by step:

```bash
git clone https://github.com/yourusername/weather-trends-forecast.git
cd weather-trends-forecast
pip install -r requirements.txt

# 1️⃣ Collect data
python scripts/collect_weather.py

# 2️⃣ Clean data
python scripts/clean_weather_data.py

# 3️⃣ Forecast temperature
python scripts/forecast_weather.py

# 4️⃣ Visualize trends
python scripts/visualize_weather.py

# 5️⃣ Generate HTML report
python scripts/generate_report.py
```

---

## ✏️ **Author**
Gyanshu Shandilya
B.Tech Computer Science Student | Data & Analytics Enthusiast

---

## 📄 **License**
MIT License – feel free to use and modify.
