import pandas as pd


def get_hourly_weather(response):
    hourly = response.Hourly()

    response_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        end =  pd.to_datetime(hourly.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    response_data["temperature_2m"] = hourly.Variables(0).ValuesAsNumpy()
    response_data["relative_humidity_2m"] = hourly.Variables(1).ValuesAsNumpy()
    response_data["weather_code"] = hourly.Variables(2).ValuesAsNumpy()
    response_data["surface_pressure"] = hourly.Variables(3).ValuesAsNumpy()
    response_data["visibility"] = hourly.Variables(4).ValuesAsNumpy()
    response_data["snow_depth"] = hourly.Variables(5).ValuesAsNumpy()
    response_data["snowfall"] = hourly.Variables(6).ValuesAsNumpy()
    response_data["showers"] = hourly.Variables(7).ValuesAsNumpy()
    response_data["rain"] = hourly.Variables(8).ValuesAsNumpy()
    response_data["precipitation"] = hourly.Variables(9).ValuesAsNumpy()
    response_data["precipitation_probability"] = hourly.Variables(10).ValuesAsNumpy()
    response_data["apparent_temperature"] = hourly.Variables(11).ValuesAsNumpy()
    response_data["wind_speed_10m"] = hourly.Variables(12).ValuesAsNumpy()
    response_data["uv_index"] = hourly.Variables(13).ValuesAsNumpy()
    response_data["uv_index_clear_sky"] = hourly.Variables(14).ValuesAsNumpy()
    response_data["sunshine_duration"] = hourly.Variables(15).ValuesAsNumpy()
    df_hourly_weather = pd.DataFrame(data = response_data)
    return df_hourly_weather