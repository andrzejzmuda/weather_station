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


def to_list(v):
    return list(v) if hasattr(v, "__iter__") else [v]


def clean_value(v):
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return float(v)
    if isinstance(v, bytes):
        return v.decode()
    return v


def concat_frames(frames):
    if isinstance(frames, pd.DataFrame):
        frames = [frames]
    if not frames:
        return pd.DataFrame({})
    if not all(isinstance(df, pd.DataFrame) for df in frames):
        raise TypeError("concat_frames: all items must be DataFrames")
    columns = [str(c) for c in frames[0].columns]
    data = {col: [] for col in columns}
    for df in frames:
        df_cols = [str(c) for c in df.columns]
        if df_cols != columns:
            raise ValueError(f"concat_frames: mismatched columns: {df_cols} != {columns}")
        for row in df.values:
            for i, col in enumerate(columns):
                data[col].append(row[i])
    return pd.DataFrame(data)