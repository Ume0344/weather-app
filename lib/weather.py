from configparser import ConfigParser
import requests
from typing import Dict, Tuple

WEATHER_API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class Weather:

    def __init__(self):
        pass

    def _get_api_key(self, configuration_file: str) -> str:
        """
        Returns the api key after fetching it from secrets.ini file.
        param configuration_file: Configuration file where api_key is stored.
        returns: API Key
        """
        config = ConfigParser()
        config.read(configuration_file)

        return config["openweather"]["api_key"]

    def get_api_url(self, city: str) -> str:
        """
        Returns the url to weather data for a city.
        param city: Name of the city to check its weather
        param api_key: API key to access  OpenWeather API.

        returns: URL to get weather data for a city
        """

        api_key = self._get_api_key(configuration_file="configuration/secrets.ini")
        api_url = f"{WEATHER_API_BASE_URL}?q={city}&appid={api_key}"

        return api_url
    
    def get_weather_data(self, city: str):
        """
        Get the weather data through api_url.
        param api_url: URL to get the data

        returns: Weather data
        """
        api_url = self.get_api_url(city=city)

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print(f"Error: Could not find weather data for this city")
            elif err.response.status_code == 401:
                print(f"Error: Access denied, check your API key")
            else:
                print(f"Error: Something went wrong getting the weather data")

        return response

    def format_weather_data(self, weather_data: Dict) -> Tuple[str, int, int]:
        """
        Format the weather data.
        param weather_data: Weather data for a city

        returns: Weather description, temperature, feels_like temperature
        """
        description = weather_data['weather'][0]['description']
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]

        return description, temperature, feels_like
