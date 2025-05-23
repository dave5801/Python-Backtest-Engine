import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['date'], index_col='date')
    df = df.sort_index()
    return df
