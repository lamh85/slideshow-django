from dotenv import dotenv_values

config = dotenv_values(".env")
open_weather_api_key = config["OPEN_WEATHER_API_KEY"]

# TODO: use these arguments
# longitude_degrees, longitude_minutes, longitude_direction, latitude_degrees, latitude_minutes, latitude_direction
def get_location_name():
  print(open_weather_api_key)

print(get_location_name())