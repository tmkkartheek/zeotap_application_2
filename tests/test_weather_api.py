# tests/test_weather_api.py
import unittest
from src.weather_api import get_weather_data, load_config

class TestWeatherAPI(unittest.TestCase):
    def test_weather_api(self):
        config = load_config()
        api_key = config['api_key']
        city = 'Delhi'
        response = get_weather_data(city, api_key)
        self.assertIn('main', response)
        self.assertIn('weather', response)

if __name__ == '__main__':
    unittest.main()
