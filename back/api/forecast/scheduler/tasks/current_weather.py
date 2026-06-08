import pandas_lite as pd
from datetime import datetime, timezone


def get_current_weather(response, geo_id=1):
    now = datetime.now(timezone.utc).isoformat()

    def val(i):
        v = response.Variables(i).Value()
        return float(v) if v is not None else None

    data = {
        "geo_id": [int(geo_id)],
        "date": [now],
        "temperature_2m": [val(0)],
        "relative_humidity_2m": [val(1)],
        "apparent_temperature": [val(2)],
        "precipitation": [val(3)],
        "rain": [val(4)],
        "showers": [val(5)],
        "snowfall": [val(6)],
        "wind_speed_10m": [val(7)],
        "wind_direction_10m": [val(8)],
        "wind_gusts_10m": [val(9)],
        "surface_pressure": [val(10)],
        "cloud_cover": [val(11)],
        "weather_code": [int(val(12))],
        "is_day": [int(val(13))]
    }

    return pd.DataFrame(data)