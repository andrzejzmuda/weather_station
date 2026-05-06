import pandas as pd


def get_15_weather(response):
    minutely15 = response.Minutely15()
    response_data = {"date": pd.date_range(
        start = pd.to_datetime(minutely15.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        end =  pd.to_datetime(minutely15.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = minutely15.Interval()),
        inclusive = "left"
    )}
    response_data["temperature_2m"] = minutely15.Variables(0).ValuesAsNumpy()
    response_data["relative_humidity_2m"] =  minutely15.Variables(1).ValuesAsNumpy()
    response_data["weather_code"] = minutely15.Variables(2).ValuesAsNumpy()
    response_data["wind_speed_10m"] = minutely15.Variables(3).ValuesAsNumpy()
    response_data["rain"] = minutely15.Variables(4).ValuesAsNumpy()
    response_data["snowfall"] = minutely15.Variables(5).ValuesAsNumpy()
    response_data["snowfall_height"] = minutely15.Variables(6).ValuesAsNumpy()
    response_data["sunshine_duration"] = minutely15.Variables(7).ValuesAsNumpy()
    response_data["visibility"] = minutely15.Variables(8).ValuesAsNumpy()
    df_response = pd.DataFrame(data = response_data)
    return df_response