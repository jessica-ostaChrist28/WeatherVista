import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        weather_data = {

            "city": data["name"],

            "temperature": data["main"]["temp"],

            "feels_like": data["main"]["feels_like"],

            "humidity": data["main"]["humidity"],

            "wind": data["wind"]["speed"],

            "condition": data["weather"][0]["main"],

            "icon": data["weather"][0]["icon"]
        }

        return weather_data

    except:
        return None
def get_forecast(city):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        forecast_data = []

        for item in data["list"][:5]:

            forecast_data.append({

                "temp": item["main"]["temp"],

                "condition": item["weather"][0]["main"],

                "icon": item["weather"][0]["icon"],

                "time": item["dt_txt"]
            })

        return forecast_data

    except:
        return None