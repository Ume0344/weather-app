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

## Get Weather Updates
- To get the weather updates for a city, run;
```
python .\main.py -c <city1_name> <city2_name> <...>
```
- To run unittests, run;
```
python .\lib\test_weather.py
```
