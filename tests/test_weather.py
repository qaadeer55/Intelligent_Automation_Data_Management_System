import json

from api.weather import get_weather


city = input("Enter City Name: ")

weather_data = get_weather(city)

print("\nWeather API Response\n")

print(json.dumps(weather_data, indent=4))