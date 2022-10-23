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
    def add_week_day(self, day_of_week_col: str) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(day_of_week_col)
            self.df.insert(date_index + 1, 'WeekDay',
                           self.df[day_of_week_col].apply(lambda x: 1 if x <= 5 else 0))

            print("Successfully Added WeekDay Column to the DataFrame")

        except Exception as e:
            print("Failed to Add WeekDay Column")

    def add_week_ends(self, day_of_week_col: str) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(day_of_week_col)
            self.df.insert(date_index + 1, 'WeekEnd',
                           self.df[day_of_week_col].apply(lambda x: 1 if x > 5 else 0))

            print("Successfully Added WeekEnd Column to the DataFrame")

        except Exception as e:
            print("Failed to Add WeekEnd Column")
    