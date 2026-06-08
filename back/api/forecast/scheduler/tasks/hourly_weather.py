import pandas_lite as pd

from forecast.scheduler.auxiliaries import generate_date_range


def get_hourly_weather(response, geo_id=1):
    hourly = response.Hourly()

    start_ts = hourly.Time() + response.UtcOffsetSeconds()
    end_ts = hourly.TimeEnd() + response.UtcOffsetSeconds()
    interval = hourly.Interval()

    dates = generate_date_range(start_ts, end_ts, interval)

    response_data = {
        "date": [d.isoformat() for d in dates],
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy().tolist(),
        "relative_humidity_2m": hourly.Variables(1).ValuesAsNumpy().tolist(),
        "weather_code": hourly.Variables(2).ValuesAsNumpy().tolist(),
        "surface_pressure": hourly.Variables(3).ValuesAsNumpy().tolist(),
        "visibility": hourly.Variables(4).ValuesAsNumpy().tolist(),
        "snow_depth": hourly.Variables(5).ValuesAsNumpy().tolist(),
        "snowfall": hourly.Variables(6).ValuesAsNumpy().tolist(),
        "showers": hourly.Variables(7).ValuesAsNumpy().tolist(),
        "rain": hourly.Variables(8).ValuesAsNumpy().tolist(),
        "precipitation": hourly.Variables(9).ValuesAsNumpy().tolist(),
        "precipitation_probability": hourly.Variables(10).ValuesAsNumpy().tolist(),
        "apparent_temperature": hourly.Variables(11).ValuesAsNumpy().tolist(),
        "wind_speed_10m": hourly.Variables(12).ValuesAsNumpy().tolist(),
        "uv_index": hourly.Variables(13).ValuesAsNumpy().tolist(),
        "uv_index_clear_sky": hourly.Variables(14).ValuesAsNumpy().tolist(),
        "sunshine_duration": hourly.Variables(15).ValuesAsNumpy().tolist(),
        "cloud_cover": hourly.Variables(16).ValuesAsNumpy().tolist(),
        "cloud_cover_low": hourly.Variables(17).ValuesAsNumpy().tolist(),
        "wind_direction_10m": hourly.Variables(18).ValuesAsNumpy().tolist(),
        "freezing_level_height": hourly.Variables(19).ValuesAsNumpy().tolist(),
        "geo_id": [geo_id] * len(dates)
    }
    cleaned = {str(k): v for k, v in response_data.items()}
    return pd.DataFrame(cleaned)