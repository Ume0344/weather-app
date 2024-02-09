import unittest
from weather import Weather
from unittest.mock import  patch


class TestWeather(unittest.TestCase):

    def test__get_api_key(self):
        w = Weather()
        api_key = w._get_api_key("configuration/test_secrets.ini")
        expected = "12345678910"

        assert api_key == expected

    @patch("weather.Weather._get_api_key")
    def test_get_api_url(self, mock_get_api_key):
        w = Weather()

        mock_get_api_key.return_value = "12345678910"

        api_url = w.get_api_url("dresden")

        expected_url = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=12345678910"

        assert api_url == expected_url

    @patch("weather.Weather.get_api_url")
    @patch("weather.requests.get")
    def test_get_weather_data_200_okay(self, mock_request_get, mock_get_api_url):
        w = Weather()

        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=dresden&appid=4cd2268194c727e8b807bf7ba72d5213"

        mock_request_get.return_value.status_code = 200
        response = w.get_weather_data("dresden")

        response.raise_for_status.assert_called_once()

        assert response.status_code == 200

    @patch("weather.Weather.get_api_url")
    @patch("weather.requests.get")
    def test_get_weather_data_404_not_found(self, mock_request_get, mock_get_api_url):
        w = Weather()

        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=blablabla&appid=0123456789103"

        mock_request_get.return_value.status_code = 404
        response = w.get_weather_data("blablabla")

        response.raise_for_status.assert_called_once()

        assert response.status_code == 404

    @patch("weather.Weather.get_api_url")
    @patch("weather.requests.get")
    def test_get_weather_data_401_access_denied(self, mock_request_get, mock_get_api_url):
        w = Weather()

        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=blablabla&appid=123456789012345"

        mock_request_get.return_value.status_code = 401
        response = w.get_weather_data("blablabla")

        response.raise_for_status.assert_called_once()

        assert response.status_code == 401

    @patch("weather.Weather.get_api_url")
    @patch("weather.requests.get")
    def test_get_weather_data_other_failed_status_codes(self, mock_request_get, mock_get_api_url):
        w = Weather()

        mock_get_api_url.return_value = "http://api.openweathermap.org/data/2.5/weather?q=blablabla&appid=12345678901"

        mock_request_get.return_value.status_code = 300
        response = w.get_weather_data("blablabla")

        response.raise_for_status.assert_called_once()

        assert response.status_code == 300


if __name__ == '__main__':
    unittest.main()
