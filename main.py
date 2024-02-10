from lib.weather import Weather
import argparse
import sys
from typing import List


def read_cli_args() -> argparse.Namespace:
    """
    Reads the CLI argument.

    Returns: argparse.Namespace
    """
    # Create a parser
    parser = argparse.ArgumentParser(
        description="Get weather  information by city name"
    )

    # Setup arguments to be parsed
    parser.add_argument(
        "-c", "--city", nargs="+", type=str, help="enter the city name"
    )

    return parser.parse_args()


def main():
    user_args = read_cli_args()
    w = Weather()

    cities: List[str] = user_args.city

    if cities is None:
        sys.exit("No city is mentioned. Please mention atleast one city")

    for city in cities:
        weather_data = w.get_weather_data(city)
        description, temperature, feels_like_temperature = w.format_weather_data(weather_data=weather_data.json())
        print(f"City: {city.capitalize()}\t{description}\tCurrent Temperature: {temperature}K\tFeels like: {feels_like_temperature}K\n")


if __name__ == "__main__":
    main()
