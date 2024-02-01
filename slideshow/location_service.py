from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
open_weather_api_key = config["OPEN_WEATHER_API_KEY"]

# TODO: use these arguments
# longitude_degrees, longitude_minutes, longitude_direction, latitude_degrees, latitude_minutes, latitude_direction
def get_location_name():
  # TODO: replace these query params with function's arguments
  response = requests.get(f'http://api.openweathermap.org/geo/1.0/reverse?lat=49.2827&lon=-123.1207&appid={open_weather_api_key}')
  return response.text
