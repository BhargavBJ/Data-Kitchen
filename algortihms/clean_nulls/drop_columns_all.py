import pandas as pd

def execute(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.dropna(axis=1, how='all')
    return cleaned_df
