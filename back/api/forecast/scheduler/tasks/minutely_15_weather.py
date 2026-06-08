import pandas_lite as pd

from forecast.scheduler.auxiliaries import generate_date_range


def get_15_weather(response, geo_id=1):
    minutely15 = response.Minutely15()

    start_ts = minutely15.Time() + response.UtcOffsetSeconds()
    end_ts = minutely15.TimeEnd() + response.UtcOffsetSeconds()
    interval = minutely15.Interval()

    dates = generate_date_range(start_ts, end_ts, interval)

    response_data = {
        "date": [d.isoformat() for d in dates],
        "temperature_2m": minutely15.Variables(0).ValuesAsNumpy().tolist(),
        "relative_humidity_2m": minutely15.Variables(1).ValuesAsNumpy().tolist(),
        "weather_code": minutely15.Variables(2).ValuesAsNumpy().tolist(),
        "wind_speed_10m": minutely15.Variables(3).ValuesAsNumpy().tolist(),
        "rain": minutely15.Variables(4).ValuesAsNumpy().tolist(),
        "snowfall": minutely15.Variables(5).ValuesAsNumpy().tolist(),
        "snowfall_height": minutely15.Variables(6).ValuesAsNumpy().tolist(),
        "sunshine_duration": minutely15.Variables(7).ValuesAsNumpy().tolist(),
        "visibility": minutely15.Variables(8).ValuesAsNumpy().tolist(),
        "showers": minutely15.Variables(9).ValuesAsNumpy().tolist(),
        "precipitation": minutely15.Variables(10).ValuesAsNumpy().tolist(),
        "wind_speed_10m": minutely15.Variables(11).ValuesAsNumpy().tolist(),
        "wind_direction_10m": minutely15.Variables(12).ValuesAsNumpy().tolist(),
        "wind_gusts_10m": minutely15.Variables(13).ValuesAsNumpy().tolist(),
        "geo_id": [geo_id] * len(dates)
    }

    return pd.DataFrame(response_data)