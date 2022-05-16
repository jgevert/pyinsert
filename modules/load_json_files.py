import json


def read_file(file_name: str) -> json:
    with open(file_name, 'r', encoding='utf-8') as f_in:
        return json.loads(f_in.read())
