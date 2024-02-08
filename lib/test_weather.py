import unittest
from lib.weather import Weather as w


class TestWeather(unittest.TestCase):
    def test_print_weather(self):
        w.print_weather

if __name__ == '__main__':
    unittest.main()
