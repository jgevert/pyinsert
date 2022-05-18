import pandas as pd


class PandasLoader:
    def __init__(self):
        self.df_list: list = []
        self.partitions: int = 1

    def into_dataframe(self, df_list: list, partitions: int = 1):
        self.partitions = partitions

