import pandas as pd


class DataManipulator:
    def __init__(self) -> None:
        pass
    
    def remove_missing_values(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        df.drop(columns=columns, inplace=True)
        return df

    def remove_all_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(inplace=True)
        return df
    