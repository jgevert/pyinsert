import dask.DataFrame as dd


class DaskDDLoader:
    def __init__(self):
        self.df_list: list = []

    def into_dask(self, df_list: list, partitions: int):
        pass