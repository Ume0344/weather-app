from lib.weather import Weather
import argparse
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

    for city in cities:
        weather_data = w.get_weather_data(city)
        print(f"{city}: {weather_data.json()}\n")


if __name__ == "__main__":
    main()
