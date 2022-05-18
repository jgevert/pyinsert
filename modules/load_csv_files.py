import pandas as pd
import glob
import json


class CSVImporter:
    """
    This class takes variables source_folder:str, files: list, sep: str and datamodel: json
    for initialization. After successful init method import_csv_files is available and will fill
    self.dataframe_list with pandas DataFrames
    """
    def __init__(self, source_folder: str, files: list, sep: str, datamodel: json, pkeys: list):
        self.source_folder: str = source_folder
        self.files: list = files
        self.files_list: list = []
        self.sep: str = sep
        self.datamodel: json = datamodel
        self.dataframe_list: list = []
        self.pkeys: list = []

    def _get_files(self) -> None:
        combination: str = ''
        all_possible_combinations = [f"{self.source_folder}/{element}" for element in self.files]
        try:
            for combination in all_possible_combinations:
                self.files_list.append(glob.glob(combination))
        except UnboundLocalError:
            print(f"Error! File {combination} not found on disk!")

    def import_csv_files(self):
        self._get_files()
        for file in self.files_to_load:
            df = pd.read_csv(file, sep=self.sep, encoding='utf-8').astype(self.datamodel)
            # data cleaning
            # make columns lower case
            new_columns = [str(name).lower() for name in df.columns]
            column_rename = dict(zip(df.columns, new_columns))
            df.rename(columns=column_rename, inplace=True)
            # drop duplicates
            df.drop_duplicates(subset=self.pkeys, inplace=True)
            # append to class list
            self.dataframe_list.append(df)
