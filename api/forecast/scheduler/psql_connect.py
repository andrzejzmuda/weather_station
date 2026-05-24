import requests
import os
import logging
from datetime import datetime, timezone

from forecast.scheduler.auxiliaries import clean_value
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


def send_weather_to_api(df, endpoint):
    for col in df.columns:
        if len(df[:, col]) > 0 and isinstance(df[0, col], datetime):
            df[col] = [df[i, col].isoformat() for i in range(len(df[:, col]))]
    unix_cols = ["sunrise", "sunset"]
    for col in unix_cols:
        if col in df.columns:
            df[col] = [
                datetime.fromtimestamp(int(df[i, col]), tz=timezone.utc).isoformat()
                if df[i, col] is not None else None
                for i in range(len(df[:, col]))
            ]

    payload = []
    rows = len(df[:, df.columns[0]])
    for i in range(rows):
        row = {}
        for col in df.columns:
            row[col] = clean_value(df[i, col])
        payload.append(row)

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