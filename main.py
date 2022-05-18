from dataclasses import dataclass
from modules import load_json_files
from modules import greb_parameters
from modules.load_csv_files import CSVImporter
from modules.load_into_pandas import PandasLoader
import json
import sys


@dataclass
class Projects:
    project_name: str
    update: bool

    def __init__(self):
        self.project_name = ''
        self.update = False


@dataclass
class Database:
    database: str
    port: int
    username: str
    password: str
    host: str
    schema: str
    table: str
    primary_keys: list
    database_type: str
    uri: str

    def __init__(self, json_file: str) -> None:
        json_content = load_json_files.read_file(json_file)
        self.host = json_content['host']
        self.port = json_content['port']
        self.username = json_content['username']
        self.password = json_content['password']
        self.schema = json_content['schema']
        self.table = json_content['table']
        self.primary_keys = json_content['primary_keys']
        self.database = json_content['database']
        self.database_type = json_content['database_type']
        # build uri
        self.uri = f"{self.database_type}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class ProjectMeta:
    source_folder: str
    files: list

    def __init__(self, project_file: str) -> None:
        json_content = load_json_files.read_file(project_file)
        self.source_folder = json_content['source_folder']
        self.files = json_content['files']


@dataclass
class Datamodel:
    model: json

    def __init__(self, datamodel_file: str) -> None:
        self.model = load_json_files.read_file(datamodel_file)


def main():
    # init process
    return_dict = greb_parameters.sys_arguments(sys.argv)
    db_conncect = Database(f"projects/{return_dict['project_name']}/database.json")
    project_meta = ProjectMeta(f"projects/{return_dict['project_name']}/project_meta.json")
    data_model = Datamodel(f"projects/{return_dict['project_name']}/datamodel.json")

    # load data into dataframes
    project_csv = CSVImporter(
        source_folder=project_meta.source_folder,
        files=project_meta.files,
        sep='|',
        datamodel=data_model.model,
        pkeys=db_conncect.primary_keys
    )

    project_csv.into_dataframes(partitions)


if __name__ == '__main__':
    main()
