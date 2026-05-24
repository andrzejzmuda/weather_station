import pandas_lite as pd

from forecast.scheduler.auxiliaries import generate_date_range


def get_daily_weather(response, geo_id=1):
    daily = response.Daily()

    start_ts = daily.Time() + response.UtcOffsetSeconds()
    end_ts = daily.TimeEnd() + response.UtcOffsetSeconds()
    interval = daily.Interval()

    dates = generate_date_range(start_ts, end_ts, interval)
    dates = [d.isoformat() for d in dates]

    response_data = {
        "date": dates,
        "weather_code": daily.Variables(0).ValuesAsNumpy().tolist(),
        "temperature_2m_max": daily.Variables(1).ValuesAsNumpy().tolist(),
        "temperature_2m_min": daily.Variables(2).ValuesAsNumpy().tolist(),
        "sunrise": daily.Variables(3).ValuesAsNumpy().tolist(),
        "sunset": daily.Variables(4).ValuesAsNumpy().tolist(),
        "precipitation_sum": daily.Variables(5).ValuesAsNumpy().tolist(),
        "rain_sum": daily.Variables(6).ValuesAsNumpy().tolist(),
        "showers_sum": daily.Variables(7).ValuesAsNumpy().tolist(),
        "snowfall_sum": daily.Variables(8).ValuesAsNumpy().tolist(),
        "wind_speed_10m_max": daily.Variables(9).ValuesAsNumpy().tolist(),
        "wind_gusts_10m_max": daily.Variables(10).ValuesAsNumpy().tolist(),
        "wind_direction_10m_dominant": daily.Variables(11).ValuesAsNumpy().tolist(),
        "geo_id": [geo_id] * len(dates)
    }

    return pd.DataFrame(response_data)