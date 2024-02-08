from lib.weather import Weather as w
from configparser import ConfigParser
import argparse


def get_api_key() -> str:
    """
    Returns the api key after fetching it from secrets.ini file.
    returns: API Key
    """
    config = ConfigParser()
    config.read("./configuration/secrets.ini")

    return config["openweather"]["api_key"]


def read_cli_args() -> argparse.Namespace:
    """
    Reads the CLI arguments.

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
    w.print_weather()
    user_args = read_cli_args()
    print(user_args)


if __name__ == "__main__":
    main()
