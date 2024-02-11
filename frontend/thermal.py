import pandas as pd

def get_last_temp(conn):
    df = pd.read_sql_query("SELECT * FROM thermal order by datetime desc limit 10", conn)
    df = df.groupby('id').head(1)
    df['datetime'] = pd.to_datetime(df.datetime, unit='s')
    out=df.to_dict(orient='records')
    return out


def get_last_entries(conn, num_entries):
    df = pd.read_sql_query(f"SELECT * FROM thermal order by datetime desc limit {num_entries}", conn)
    df['datetime'] = pd.to_datetime(df.datetime, unit='s')
    return df