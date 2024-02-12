# weather-app

In this project, we are going to use OpenWeather API to build a weather App. We use API to get the [weather details by city](https://openweathermap.org/current#name).

To use the API by city name;
```
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```

## Get an API key
- Sign up at [OpenWeather](https://home.openweathermap.org/users/sign_up) and get the API key. The API key takes couple of minutes to be activated. 
- Check if API key is activated by calling API through http client. i,e.
```
curl "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
```
- To get the temperature in Celsius;
```
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=metric
```

## Get the dependencies through requirements.txt
- To create requirements.txt file, run from project root directory;
```
pip freeze > requirements.txt
```
- To get all the dependecies, run from project root directory;
```
pip install -r requirements.txt
```

## Get Weather Updates
- To get help on how to run the project, run;
```
python main.py --help
```

- To get the weather updates for a city in kelvin, run;
```
python .\main.py -c <city1_name> <city2_name> <...>
```

- To get the weather updates for a city in fahrenheit, run;
```
python .\main.py -c <city1_name> <city2_name> <...> -f
```

- To get the weather updates for a city in celcius, run;
```
python .\main.py -c <city1_name> <city2_name> <...> -cel
```

- To run unittests, run from project root directory;
```
coverage run .\lib\test_weather.py
coverage report -m
```
