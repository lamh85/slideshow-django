from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
open_weather_api_key = config["OPEN_WEATHER_API_KEY"]

# TODO: use these arguments
# longitude_degrees, longitude_minutes, longitude_direction, latitude_degrees, latitude_minutes, latitude_direction
# Vancouver, BC: 49.277933762813475 latitude, -123.1093055007045 longitude
def get_location_name(params):
    coordinates_decimal = get_coordinates_decimal(params)
    latitude_decimal = coordinates_decimal["latitude"]
    longitude_decimal = coordinates_decimal["longitude"]

    response = requests.get(f'http://api.openweathermap.org/geo/1.0/reverse?lat={latitude_decimal}&lon={longitude_decimal}&appid={open_weather_api_key}')
    return response.text

def get_coordinates_decimal(params):
    # Match these params with https://github.com/exif-js/exif-js
    latitude_degrees = params["latitude_degrees"]
    latitude_minutes = params["latitude_minutes"]
    latitude_direction = params["latitude_direction"]
    longitude_degrees = params["longitude_degrees"]
    longitude_minutes = params["longitude_minutes"]
    longitude_direction = params["longitude_direction"]

    latitude = get_dimension_decimal(latitude_degrees, latitude_minutes, latitude_direction)
    longitude = get_dimension_decimal(longitude_degrees, longitude_minutes, longitude_direction)

    return { "latitude": latitude, "longitude": longitude }

def get_dimension_decimal(degrees, minutes, direction):
    multiplier = 1 if direction == "N" or direction == "E" else -1
    return multiplier * (degrees + minutes / 60)