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

    # action=store_true will set imperial=true if flag is entered by user, Otherwise it is false.
    parser.add_argument(
        "-f", "--fahrenheit", action="store_true", help="displays temperature in fahrenheit"
    )

    parser.add_argument(
        "-cel", "--celcius", action="store_true", help="displays temperature in celcius"
    )

    return parser.parse_args()


def main():
    user_args = read_cli_args()
    w = Weather()

    fahrenheit_flag = user_args.fahrenheit
    celcius_flag = user_args.celcius

    cities: List[str] = user_args.city

    if cities is None:
        sys.exit("No city is mentioned. Please mention atleast one city")

    for city in cities:
        weather_data = w.get_weather_data(city, fahrenheit_flag, celcius_flag)

        description, temperature, feels_like_temperature = w.format_weather_data(weather_data=weather_data.json())

        if fahrenheit_flag:
            # Unit is fahrenheit
            print(f"City: {city.capitalize()}\t{description}\tCurrent Temperature: {temperature}°F\tFeels like: {feels_like_temperature}°F\n")
        elif celcius_flag:
            # Unit is celcius
            print(f"City: {city.capitalize()}\t{description}\tCurrent Temperature: {temperature}°C\tFeels like: {feels_like_temperature}°C\n")
        else:
            # Unit is kelvin
            print(f"City: {city.capitalize()}\t{description}\tCurrent Temperature: {temperature}K\tFeels like: {feels_like_temperature}K\n")


if __name__ == "__main__":
    main()
