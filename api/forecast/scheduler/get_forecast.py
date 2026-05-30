import pandas_lite as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry
from forecast.scheduler.auxiliaries import concat_frames

from forecast.models import GeoData
from forecast.scheduler.tasks.geo_data import get_geographic_data
from forecast.scheduler.tasks.current_weather import get_current_weather
from forecast.scheduler.tasks.minutely_15_weather import get_15_weather
from forecast.scheduler.tasks.hourly_weather import get_hourly_weather
from forecast.scheduler.tasks.daily_weather import get_daily_weather
from forecast.scheduler.psql_connect import (send_geo_to_api,
                                                send_weather_to_api)




def get_weather(latitude=51.19, longitude=16.19):
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min",
                   "apparent_temperature_max", "apparent_temperature_min",
                   "sunrise", "sunset", "daylight_duration", "sunshine_duration",
                   "wind_speed_10m_max", "wind_gusts_10m_max", "rain_sum",
                   "showers_sum", "snowfall_sum", "precipitation_sum",
                   "precipitation_hours", "precipitation_probability_max",
                   "temperature_2m_mean", "surface_pressure_mean",
                   "precipitation_probability_mean", "cloud_cover_min",
                   "cloud_cover_max", "cloud_cover_mean", "visibility_max",
                   "visibility_min", "visibility_mean"],
        "hourly": ["temperature_2m", "relative_humidity_2m", "weather_code",
                   "surface_pressure", "visibility", "snow_depth",
                   "snowfall", "showers", "rain", "precipitation",
                   "precipitation_probability", "apparent_temperature",
                   "wind_speed_10m", "uv_index", "uv_index_clear_sky",
                   "sunshine_duration", "cloud_cover", "cloud_cover_low",
                   "wind_direction_10m", "freezing_level_height"],
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature",
                    "precipitation", "rain", "showers", "snowfall", "wind_speed_10m",
                    "wind_direction_10m", "wind_gusts_10m", "surface_pressure",
                    "cloud_cover", "weather_code", "is_day"],
        "minutely_15": ["temperature_2m", "relative_humidity_2m", "weather_code",
                        "wind_speed_10m", "rain", "snowfall", "snowfall_height",
                        "sunshine_duration", "visibility", "showers", "precipitation",
                        "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
        "timezone": "Europe/Berlin",
        "past_days": 0,
        "forecast_days": 7,
        "forecast_minutely_15": 4,
        "past_minutely_15": 0,
    }
    responses = openmeteo.weather_api(url, params = params)
    response = responses[0]
    return response


def get_geo():
    response = get_weather()
    df_geographic = get_geographic_data(response)
    send_geo_to_api(df_geographic)
    return "Geographic data sent to API"


def get_current():
    frames = []
    for n in GeoData.objects.all():
        response = get_weather(n.latitude, n.longitude)
        df_current = get_current_weather(response.Current(), n.id)
        frames.append(df_current)
    send_weather_to_api(concat_frames(frames), "currentweather/")
    return "Current weather data sent to API"


def get_minutely_15():
    frames = []
    for n in GeoData.objects.all():
        response = get_weather(n.latitude, n.longitude)
        df_minutely_15 = get_15_weather(response, n.id)
        frames.append(df_minutely_15)
    send_weather_to_api(concat_frames(frames), "minutely15weather/")
    return "Minutely 15 weather data sent to API"


def get_hourly():
    frames = []
    for n in GeoData.objects.all():
        response = get_weather(n.latitude, n.longitude)
        df_hourly = get_hourly_weather(response, n.id)
        frames.append(df_hourly)
    send_weather_to_api(concat_frames(frames), "hourlyweather/")
    return "Hourly weather data sent to API"


def get_daily():
    frames = []
    for n in GeoData.objects.all():
        response = get_weather(n.latitude, n.longitude)
        df_daily = get_daily_weather(response, n.id)
        frames.append(df_daily)
    send_weather_to_api(concat_frames(frames), "dailyweather/")
    return "Daily weather data sent to API"