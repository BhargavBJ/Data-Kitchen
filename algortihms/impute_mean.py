import pandas as pd

def execute(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].mean())

    return cleaned_df