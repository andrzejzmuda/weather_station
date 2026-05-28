import pandas_lite as pd

from forecast.scheduler.auxiliaries import generate_date_range


def get_daily_weather(response, geo_id=1):
    daily = response.Daily()

    start_ts = daily.Time() + response.UtcOffsetSeconds()
    end_ts = daily.TimeEnd() + response.UtcOffsetSeconds()
    interval = daily.Interval()

    dates = generate_date_range(start_ts, end_ts, interval)

    response_data = {
        "date": [d.isoformat() for d in dates],
        "weather_code": daily.Variables(0).ValuesAsNumpy().tolist(),
        "temperature_2m_max": daily.Variables(1).ValuesAsNumpy().tolist(),
        "temperature_2m_min": daily.Variables(2).ValuesAsNumpy().tolist(),
        "apparent_temperature_max": daily.Variables(3).ValuesAsNumpy().tolist(),
        "apparent_temperature_min": daily.Variables(4).ValuesAsNumpy().tolist(),
        "sunrise": daily.Variables(5).ValuesAsNumpy().tolist(),
        "sunset": daily.Variables(6).ValuesAsNumpy().tolist(),
        "daylight_duration": daily.Variables(7).ValuesAsNumpy().tolist(),
        "sunshine_duration": daily.Variables(8).ValuesAsNumpy().tolist(),
        "wind_speed_10m_max": daily.Variables(9).ValuesAsNumpy().tolist(),
        "wind_gusts_10m_max": daily.Variables(10).ValuesAsNumpy().tolist(),
        "rain_sum": daily.Variables(11).ValuesAsNumpy().tolist(),
        "showers_sum": daily.Variables(12).ValuesAsNumpy().tolist(),
        "snowfall_sum": daily.Variables(13).ValuesAsNumpy().tolist(),
        "precipitation_sum": daily.Variables(14).ValuesAsNumpy().tolist(),
        "precipitation_hours": daily.Variables(15).ValuesAsNumpy().tolist(),
        "precipitation_probability_max": daily.Variables(16).ValuesAsNumpy().tolist(),
        "temperature_2m_mean": daily.Variables(17).ValuesAsNumpy().tolist(),
        "surface_pressure_mean": daily.Variables(18).ValuesAsNumpy().tolist(),
        "precipitation_probability_mean": daily.Variables(19).ValuesAsNumpy().tolist(),
        "cloud_cover_min": daily.Variables(20).ValuesAsNumpy().tolist(),
        "cloud_cover_max": daily.Variables(21).ValuesAsNumpy().tolist(),
        "cloud_cover_mean": daily.Variables(22).ValuesAsNumpy().tolist(),
        "visibility_max": daily.Variables(23).ValuesAsNumpy().tolist(),
        "visibility_min": daily.Variables(24).ValuesAsNumpy().tolist(),
        "visibility_mean": daily.Variables(25).ValuesAsNumpy().tolist(),
        "geo_id": [geo_id] * len(dates)
    }

    return pd.DataFrame(response_data)