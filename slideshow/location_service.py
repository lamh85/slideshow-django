from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
open_weather_api_key = config["OPEN_WEATHER_API_KEY"]

# TODO: use these arguments
# longitude_degrees, longitude_minutes, longitude_direction, latitude_degrees, latitude_minutes, latitude_direction
# Vancouver, BC: 49.277933762813475 latitude, -123.1093055007045 longitude
def get_location_name(params):
    latitude_degrees = params["latitude_degrees"]
    longitude_degrees = params["longitude_degrees"]

    response = requests.get(f'http://api.openweathermap.org/geo/1.0/reverse?lat={latitude_degrees}&lon={longitude_degrees}&appid={open_weather_api_key}')
    return response.text
