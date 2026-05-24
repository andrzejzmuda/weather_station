import pandas_lite as pd


def get_geographic_data(response):
    geographic = {
        "latitude": response.Latitude(),
        "longitude": response.Longitude(),
        "elevation": response.Elevation(),
        "timezone": response.Timezone(),
        "timezone_abbreviation": response.TimezoneAbbreviation(),
        "utc_offset_seconds": response.UtcOffsetSeconds(),
    }
    df_geo = pd.DataFrame([geographic])
    return df_geo