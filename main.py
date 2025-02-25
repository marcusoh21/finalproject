import sqlite3   # For SQLite database operations  
import requests  # For making API requests  
import datetime   # For handling dates
import json       # For handling JSON data from the API  
import os         # For checking file existence
import crud

# OpenWeather API key
API_KEY = "9994ae8d73909ba97a0e41187ce67b24"

# South Pole coordinates
LAT, LON = -90.0000, 0.0000

# OpenWeather API URL
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# --- Fetch Weather Data ---
def fetch_weather():
    """Fetch weather data from OpenWeather API."""
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return {
            "date": datetime.date.today().isoformat(),
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    else:
        print("Error fetching data:", response.status_code)
        return None

def fetch_and_store_weather():
    """Fetch weather data and store it in the database."""
    weather_data = fetch_weather()
    if weather_data:
        crud.insert_entry(weather_data)
        print("Weather data fetched and stored successfully.")
    else:
        print("Failed to fetch weather data.")

# --- Temporary Testing Code (Commented Out) ---
# Test fetching data manually
# test_data = fetch_weather()
# if test_data:
#     print("Fetched weather data successfully:", test_data)

# Example of inserting fetched data into the database (manually tested before)
# if test_data:
#     crud.insert_entry(test_data)
#     print("Inserted test data into the database.")
