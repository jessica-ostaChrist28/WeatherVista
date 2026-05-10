import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


# ==============================
# CITY WEATHER
# ==============================

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        return format_weather_data(data)

    except Exception as e:
        print("Weather Error:", e)
        return None


# ==============================
# GEOLOCATION WEATHER
# ==============================

def get_weather_by_location(lat, lon):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}"
        f"&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        return format_weather_data(data)

    except Exception as e:
        print("Location Weather Error:", e)
        return None


# ==============================
# FORECAST
# ==============================

def get_forecast(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return []

        data = response.json()

        forecast_data = []

        for item in data["list"][:8]:

            forecast_data.append({

                "temp": round(item["main"]["temp"]),

                "condition": item["weather"][0]["main"],

                "icon": item["weather"][0]["icon"],

                "time": item["dt_txt"]
            })

        return forecast_data

    except Exception as e:
        print("Forecast Error:", e)
        return []


# ==============================
# FORMAT WEATHER DATA
# ==============================

def format_weather_data(data):

    return {

        "city": data["name"],

        "temperature": round(data["main"]["temp"]),

        "feels_like": round(data["main"]["feels_like"]),

        "humidity": data["main"]["humidity"],

        "wind": data["wind"]["speed"],

        "condition": data["weather"][0]["main"],

        "description": data["weather"][0]["description"],

        "icon": data["weather"][0]["icon"]
    }