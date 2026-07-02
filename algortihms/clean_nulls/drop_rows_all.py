import pandas as pd
def execute(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.dropna(how= 'all')
    return cleaned_df