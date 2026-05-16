import psycopg2
import requests
import pandas as pd
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT")
        )
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print(f"Error occurred while connecting to database: {e}")
        return None


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
    return response.status_code, response.text