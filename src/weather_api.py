# src/weather_api.py

import requests
import yaml

def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for 4xx/5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city_name}: {e}")
        return {}

def load_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)
