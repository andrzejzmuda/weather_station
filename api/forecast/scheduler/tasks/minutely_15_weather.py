import pandas_lite as pd

from forecast.scheduler.auxiliaries import generate_date_range


def get_15_weather(response, geo_id=1):
    minutely15 = response.Minutely15()

    start_ts = minutely15.Time() + response.UtcOffsetSeconds()
    end_ts = minutely15.TimeEnd() + response.UtcOffsetSeconds()
    interval = minutely15.Interval()

    dates = generate_date_range(start_ts, end_ts, interval)

    response_data = {
        "date": dates,
        "temperature_2m": minutely15.Variables(0).ValuesAsNumpy(),
        "relative_humidity_2m": minutely15.Variables(1).ValuesAsNumpy(),
        "weather_code": minutely15.Variables(2).ValuesAsNumpy(),
        "wind_speed_10m": minutely15.Variables(3).ValuesAsNumpy(),
        "rain": minutely15.Variables(4).ValuesAsNumpy(),
        "snowfall": minutely15.Variables(5).ValuesAsNumpy(),
        "snowfall_height": minutely15.Variables(6).ValuesAsNumpy(),
        "sunshine_duration": minutely15.Variables(7).ValuesAsNumpy(),
        "visibility": minutely15.Variables(8).ValuesAsNumpy(),
        "geo_id": [geo_id] * len(dates)
    }

    df_response = pd.DataFrame(response_data)
    return df_response