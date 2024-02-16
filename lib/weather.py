from configparser import ConfigParser
import requests
from requests.models import Response
from typing import Dict, Tuple
import sys

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

    def get_api_url(self, city: str, fahrenheit_flag: bool = False, celcius_flag: bool = False) -> str:
        """
        Returns the url to weather data for a city.
        param city: Name of the city to check its weather
        param api_key: API key to access  OpenWeather API.

        returns: URL to get weather data for a city according to unit of measurement.
        """

        api_url = ""
        api_key = self._get_api_key(configuration_file="configuration/secrets.ini")

        if fahrenheit_flag == False and celcius_flag == False:
            api_url = f"{WEATHER_API_BASE_URL}?q={city}&appid={api_key}"
        elif fahrenheit_flag == True and celcius_flag == False:
            api_url = f"{WEATHER_API_BASE_URL}?q={city}&appid={api_key}&units=imperial"
        elif fahrenheit_flag == False and celcius_flag == True:
            api_url = f"{WEATHER_API_BASE_URL}?q={city}&appid={api_key}&units=metric"
        elif fahrenheit_flag == True and celcius_flag == True:
            print(f"You entered celcius and fahrenheit. Showing results in celcius only. Please enter only one unit of measurement")
            api_url = f"{WEATHER_API_BASE_URL}?q={city}&appid={api_key}&units=metric"
        
        return api_url
    
    def get_weather_data(self, city: str, fahrenheit_flag: bool = False, celcius_flag: bool = False) -> Response:
        """
        Get the weather data through api_url.
        param api_url: URL to get the data

        returns: Weather data
        """
        api_url = self.get_api_url(city=city, fahrenheit_flag=fahrenheit_flag, celcius_flag=celcius_flag)

        try:
            response = requests.get(api_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                sys.exit(f"Error: Could not find weather data for this city")
            elif err.response.status_code == 401:
                sys.exit(f"Error: Access denied, check your API key")
            else:
                sys.exit(f"Error: Something went wrong getting the weather data")

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
