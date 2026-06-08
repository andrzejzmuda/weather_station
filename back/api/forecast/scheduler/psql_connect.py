import requests
import os
import logging
from datetime import datetime, timezone
from pandas_lite import DataFrame

from forecast.scheduler.auxiliaries import (
    clean_value, dataframe_to_dict, normalize_and_fill,
    dict_to_records
)
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
logger = logging.getLogger("weather")


def send_geo_to_api(df):
    url = os.getenv("URL") + "geodata/"
    payload = {
        k: clean_value(v) for k, v
        in df.to_dict(orient="records")[0].items()
    }

    headers = {
        "Authorization": f"Token {os.getenv('API_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    logger.info(f"Saving Geo Data...")
    logger.info(f"datetime: {datetime.now()}")
    logger.info(f"STATUS: {response.status_code}")
    logger.info(f"Finished saving Geo Data.")
    logger.info(f"*****************************")
    return response.status_code, response.text


def send_weather_to_api(data, endpoint):
    if isinstance(data, DataFrame):
        data = dataframe_to_dict(data)
    elif not isinstance(data, dict):
        raise TypeError("send_weather_to_api() expects dict or pandas_lite.DataFrame")
    data = normalize_and_fill(data)
    data = dict_to_records(data)
    unix_cols = {"sunrise", "sunset"}

    for rec in data:
        for key, val in rec.items():
            if hasattr(val, "item"):
                val = val.item()
            if hasattr(val, "isoformat"):
                val = val.isoformat()
            if key in unix_cols and isinstance(val, (int, float)):
                val = datetime.fromtimestamp(val, tz=timezone.utc).isoformat()
            rec[key] = val

    headers = {
        "Authorization": f"Token {os.getenv('API_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    url = os.getenv("URL") + endpoint
    response = requests.post(url, json=data, headers=headers)
    with open("last_sent.json", "w") as f:
        import json
        json.dump(data, f, indent=2)

    logger.info(f"Saving Weather Data...")
    logger.info(f"{endpoint}: datetime: {datetime.now()}")
    logger.info(f"STATUS: {response.status_code}")
    logger.info(f"Finished saving Weather Data.")
    logger.info(f"*****************************")
    return response.status_code, response.text
