import pandas as pd
from datetime import datetime

def get_current_weather(response):
    current_weather = {
        "date": datetime.now(),
        "temperature_2m": response.Variables(0).Value(),
        "relative_humidity_2m": response.Variables(1).Value(),
        "apparent_temperature": response.Variables(2).Value(),
        "precipitation": response.Variables(3).Value(),
        "rain": response.Variables(4).Value(),
        "showers": response.Variables(5).Value(),
        "snowfall": response.Variables(6).Value(),
        "wind_speed_10m": response.Variables(7).Value(),
        "wind_direction_10m": response.Variables(8).Value(),
        "wind_gusts_10m": response.Variables(9).Value(),
        "surface_pressure": response.Variables(10).Value(),
        "cloud_cover": response.Variables(11).Value(),
        "weather_code": response.Variables(12).Value(),
        "is_day": response.Variables(13).Value()
    }
    df_current = pd.DataFrame([current_weather])
    return df_current