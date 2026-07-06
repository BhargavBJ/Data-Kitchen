import pandas as pd

def execute(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    cleaned_df = df.dropna(subset=[column_name])
    return cleaned_df