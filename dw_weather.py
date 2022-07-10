import requests
from geopy.geocoders import Nominatim


def get_weather_dict(lon: float, lat: float) -> dict:
    try:
        weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly' \
                      f'=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,surface_pressure,' \
                      f'precipitation,rain,showers,snowfall,weathercode,snow_depth,cloudcover,shortwave_radiation,' \
                      f'direct_normal_irradiance,windspeed_10m,winddirection_10m,windgusts_10m&daily=weathercode,' \
                      f'temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,' \
                      f'sunrise,sunset,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,' \
                      f'windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum,' \
                      f'et0_fao_evapotranspiration&current_weather=true' \
                      f'&windspeed_unit=ms&timeformat=unixtime&timezone' \
                      f'=Europe%2FLondon&past_days=1'
        resp = requests.get(weather_url)
        return resp.json()
    except Exception as ex:
        print(ex)


def loc_to_coord(city_name: str):
    location_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&language=ru"
    resp = requests.get(location_url)
    return [resp.json()['results'][0]['latitude'], resp.json()['results'][0]['longitude']]
