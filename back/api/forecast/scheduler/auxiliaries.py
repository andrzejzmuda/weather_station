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


def dataframe_to_dict(df: pd.DataFrame) -> dict:
    data = {}
    for col_idx, col_name in enumerate(df.columns):
        data[col_name] = [row[col_idx] for row in df.values]
    return data


def normalize_and_fill(data: dict) -> dict:
    lengths = {k: len(v) for k, v in data.items() if isinstance(v, list)}
    target_len = max(lengths.values())
    fixed = {}
    for key, value in data.items():
        if not isinstance(value, list):
            fixed[key] = [value] * target_len
            continue
        cur_len = len(value)
        if cur_len == target_len:
            fixed[key] = value
        elif cur_len < target_len:
            missing = target_len - cur_len
            if all(isinstance(x, (int, float)) or x is None for x in value):
                fill_value = None
            elif all(isinstance(x, str) or x is None for x in value):
                fill_value = ""
            else:
                fill_value = None
            fixed[key] = value + [fill_value] * missing
        else:
            fixed[key] = value[:target_len]
    return fixed


def dict_to_records(data: dict) -> list[dict]:
    keys = list(data.keys())
    length = len(next(v for v in data.values() if isinstance(v, list)))
    records = []
    for i in range(length):
        rec = {}
        for k in keys:
            v = data[k]
            rec[k] = v[i] if isinstance(v, list) else v
        records.append(rec)
    return records