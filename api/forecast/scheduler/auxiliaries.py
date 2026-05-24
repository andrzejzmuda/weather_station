from datetime import datetime, timedelta, timezone
import pandas_lite as pd
import numpy as np


def generate_date_range(start_ts, end_ts, interval_seconds):
    start = datetime.fromtimestamp(start_ts, tz=timezone.utc)
    end = datetime.fromtimestamp(end_ts, tz=timezone.utc)
    delta = timedelta(seconds=interval_seconds)

    dates = []
    current = start
    while current < end:
        dates.append(current)
        current += delta

    return dates


def clean_value(v):
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return float(v)
    if isinstance(v, bytes):
        return v.decode()
    return v


def concat_frames(frames):
    if not frames:
        return pd.DataFrame({})
    columns = frames[0].columns
    data = {col: [] for col in columns}
    for df in frames:
        rows = len(df[:, columns[0]])
        for i in range(rows):
            for col in columns:
                data[col].append(df[i, col])
    return pd.DataFrame(data)