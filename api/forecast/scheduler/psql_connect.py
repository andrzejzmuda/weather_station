import requests
import pandas as pd
import os
import logging
from datetime import datetime

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
logger = logging.getLogger("weather")


def clean_bytes(obj):
    if isinstance(obj, bytes):
        return obj.decode()
    return obj


def send_geo_to_api(df):
    url = os.getenv("URL") + "geodata/"
    payload = {
        k: clean_bytes(v) for k, v
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


def send_weather_to_api(df, endpoint):
    dt_time_cols = df.select_dtypes(include=["datetime64[ns]", "datetime64[ns, UTC]"]).columns
    df[dt_time_cols] = df[dt_time_cols].astype(str)
    unix_cols = ["sunrise", "sunset"]
    for col in unix_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], unit="s", utc=True)\
                .dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    payload = df.to_dict(orient="records")

    headers = {
        "Authorization": f"Token {os.getenv('API_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url = os.getenv("URL") + endpoint
    response = requests.post(url, json=payload, headers=headers)
    logger.info(f"Saving Weather Data...")
    logger.info(f"{endpoint}: datetime: {datetime.now()}")
    logger.info(f"STATUS: {response.status_code}")
    logger.info(f"Finished saving Weather Data.")
    logger.info(f"*****************************")
    return response.status_code, response.text