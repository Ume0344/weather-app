import unittest
from weather import Weather
from unittest.mock import  patch, Mock
import requests
from requests.models import Response


class TestWeather(unittest.TestCase):

    def test__get_api_key(self):
        w = Weather()
        api_key = w._get_api_key("configuration/test_secrets.ini")
        expected = "12345678910"

        assert api_key == expected

    @patch("weather.Weather._get_api_key")
    def test_get_api_url_kelvin(self, mock_get_api_key):
        w = Weather()

        mock_get_api_key.return_value = "12345678910"

        api_url = w.get_api_url("dresden", fahrenheit_flag=False, celcius_flag=False)

        expected_url = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=12345678910"

        assert api_url == expected_url
    
    @patch("weather.Weather._get_api_key")
    def test_get_api_url_celcius(self, mock_get_api_key):
        w = Weather()

        mock_get_api_key.return_value = "12345678910"

        api_url = w.get_api_url("dresden", fahrenheit_flag=False, celcius_flag=True)

        expected_url = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=12345678910&units=metric"

        assert api_url == expected_url
    
    @patch("weather.Weather._get_api_key")
    def test_get_api_url_fahrenheit(self, mock_get_api_key):
        w = Weather()

        mock_get_api_key.return_value = "12345678910"

        api_url = w.get_api_url("dresden", fahrenheit_flag=True, celcius_flag=False)

        expected_url = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=12345678910&units=imperial"

        assert api_url == expected_url

    @patch("weather.Weather._get_api_key")
    def test_get_api_url_entered_two_units(self, mock_get_api_key):
        w = Weather()

        mock_get_api_key.return_value = "12345678910"

        api_url = w.get_api_url("dresden", fahrenheit_flag=True, celcius_flag=True)

        expected_url = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=12345678910&units=metric"

        assert api_url == expected_url

    @patch("weather.Weather.get_api_url")
    @patch("requests.get")
    def test_get_weather_data_200(self, mock_request, mock_get_api_url):
        mock_response = Mock()
        mock_response.status_code = 200

        w = Weather()
        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=01234567819"
        mock_request.return_value = mock_response

        response = w.get_weather_data("city", True, False)

        assert response.status_code == 200

    @patch("weather.Weather.get_api_url")
    @patch("requests.get")
    def test_get_weather_data_404(self, mock_request, mock_get_api_url):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_response.status_code = 404

        w = Weather()
        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=01234567819"
        mock_request.return_value = mock_response

        with self.assertRaises(SystemExit) as context:
            w.get_weather_data("city", True, False)

        self.assertIn("Error: Could not find weather data for this city", str(context.exception))

    @patch("weather.Weather.get_api_url")
    @patch("requests.get")
    def test_get_weather_data_401(self, mock_request, mock_get_api_url):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_response.status_code = 401

        w = Weather()
        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=01234567819"
        mock_request.return_value = mock_response

        with self.assertRaises(SystemExit) as context:
            w.get_weather_data("city", True, False)

        self.assertEqual("Error: Access denied, check your API key", str(context.exception))

    @patch("weather.Weather.get_api_url")
    @patch("requests.get")
    def test_get_weather_data_other_error_codes(self, mock_request, mock_get_api_url):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(response=mock_response)
        mock_response.status_code = 400

        w = Weather()
        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=01234567819"
        mock_request.return_value = mock_response

        with self.assertRaises(SystemExit) as context:
            w.get_weather_data("city", True, False)

        self.assertIn("Error: Something went wrong getting the weather data", str(context.exception))

    def test_format_weather_data(self):
        w = Weather()

        weather_data = {
            'coord': {'lon': 13.7383, 'lat': 51.0509},
            'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
            'base': 'stations',
            'main': {'temp': 285.16, 'feels_like': 284.74, 'temp_min': 282.74, 'temp_max': 287.45, 'pressure': 983, 'humidity': 89},
            'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 150}, 'clouds': {'all': 0}, 'dt': 1707564620,
            'sys': {'type': 2, 'id': 2042201, 'country': 'DE', 'sunrise': 1707546508, 'sunset': 1707581411},
            'timezone': 3600, 'id': 2935022, 'name': 'Dresden', 'cod': 200
            }

        description, temp, feels_like = w.format_weather_data(weather_data=weather_data)

        assert description == 'clear sky'
        assert temp == 285.16
        assert feels_like == 284.74


if __name__ == '__main__':
    unittest.main()
