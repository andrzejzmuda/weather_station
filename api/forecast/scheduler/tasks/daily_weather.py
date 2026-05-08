import pandas as pd


def get_daily_weather(response, geo_id=1):
    daily = response.Daily()

    response_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        end =  pd.to_datetime(daily.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    response_data["weather_code"] = daily.Variables(0).ValuesAsNumpy()
    response_data["temperature_2m_max"] = daily.Variables(1).ValuesAsNumpy()
    response_data["temperature_2m_min"] = daily.Variables(2).ValuesAsNumpy()
    response_data["apparent_temperature_max"] = daily.Variables(3).ValuesAsNumpy()
    response_data["apparent_temperature_min"] = daily.Variables(4).ValuesAsNumpy()
    response_data["sunrise"] = daily.Variables(5).ValuesInt64AsNumpy()
    response_data["sunset"] = daily.Variables(6).ValuesInt64AsNumpy()
    response_data["daylight_duration"] = daily.Variables(7).ValuesAsNumpy()
    response_data["sunshine_duration"] = daily.Variables(8).ValuesAsNumpy()
    response_data["wind_speed_10m_max"] = daily.Variables(9).ValuesAsNumpy()
    response_data["wind_gusts_10m_max"] = daily.Variables(10).ValuesAsNumpy()
    response_data["rain_sum"] = daily.Variables(11).ValuesAsNumpy()
    response_data["showers_sum"] = daily.Variables(12).ValuesAsNumpy()
    response_data["snowfall_sum"] = daily.Variables(13).ValuesAsNumpy()
    response_data["precipitation_sum"] = daily.Variables(14).ValuesAsNumpy()
    response_data["precipitation_hours"] = daily.Variables(15).ValuesAsNumpy()
    response_data["precipitation_probability_max"] = daily.Variables(16).ValuesAsNumpy()
    response_data["temperature_2m_mean"] = daily.Variables(17).ValuesAsNumpy()
    response_data["surface_pressure_mean"] = daily.Variables(18).ValuesAsNumpy()
    response_data["precipitation_probability_mean"] = daily.Variables(19).ValuesAsNumpy()
    response_data["cloud_cover_min"] = daily.Variables(20).ValuesAsNumpy()
    response_data["cloud_cover_max"] = daily.Variables(21).ValuesAsNumpy()
    response_data["cloud_cover_mean"] = daily.Variables(22).ValuesAsNumpy()
    response_data["visibility_max"] = daily.Variables(23).ValuesAsNumpy()
    response_data["visibility_min"] = daily.Variables(24).ValuesAsNumpy()
    response_data["visibility_mean"] = daily.Variables(25).ValuesAsNumpy()
    response_data["geo_id"] = [geo_id] * len(response_data["date"])
    df_daily_weather = pd.DataFrame(data = response_data)
    return df_daily_weather