import json
import requests
import urllib.request
from settings import *


def get_location_data():
    try:
        with urllib.request.urlopen("https://ipapi.co/json/") as url:
            data = json.loads(url.read().decode())
            return (data["city"], data["country"], data["latitude"], data["longitude"])
    except:
        pass


def get_weather_data(latitude, longitude, units, period):
    # CALL API.
    url = f"{BASE_URL}&lat={latitude}&lon={longitude}&units={units}&appid={API_KEY}"
    respone = requests.get(url)
    # GET DATA.
    today_data = {}
    forecast_data = {}

    if respone.status_code == 200:
        data = respone.json()
        # TODAY.
        for index, entry in enumerate(data["list"]):
            if index == 0:
                today_data = {
                    "temp": round(entry["main"]["temp"], 0),
                    "feels_like": round(entry["main"]["feels_like"], 0),
                    "weather": entry["weather"][0]["main"],
                }
                today = entry["dt_txt"].split(" ")[0]
            else:
                if entry["dt_txt"].split(" ")[0] != today:
                    milestone = index + 4
                    break
        # FORECAST.
        for index in range(milestone, len(data["list"]), 8):
            entry = data["list"][index]
            forecast_data[entry["dt_txt"].split(" ")[0]] = {
                "temp": round(entry["main"]["temp"], 0),
                "feels_like": round(entry["main"]["feels_like"], 0),
                "weather": entry["weather"][0]["main"],
            }

    return today_data if period == "today" else forecast_data
