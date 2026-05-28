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
    unix_cols = ["sunrise", "sunset"]

    # konwersja unix → iso
    for col in unix_cols:
        if col in df.columns:
            col_index = df.columns.index(col)
            for row in df.values:
                val = row[col_index]
                if val not in (None, ""):
                    row[col_index] = datetime.fromtimestamp(
                        int(val), tz=timezone.utc
                    ).isoformat()
                else:
                    row[col_index] = None

    # budowanie payload
    payload = []
    columns = df.columns
    for row in df.values:
        record = {}
        for i, col in enumerate(columns):
            record[col] = clean_value(row[i])
        payload.append(record)

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
