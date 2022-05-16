from dataclasses import dataclass
from modules import load_json_files


@dataclass
class Database:
    port: int
    username: str
    password: str
    host: str
    schema: str
    table: str
    primary_keys: list


@dataclass
class Project:
    source_folder: str
    files: list


@dataclass
class Datamodel:
    model: str


def main():
    pass


if __name__ == '__main__':
    main()
