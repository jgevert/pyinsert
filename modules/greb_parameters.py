def sys_arguments(sys_args: list) -> dict:
    project_setup = {"-p": "project_name", "-u": "update", "-dp": "dataprotection"}
    return_dict = {"project_name": "", "update": False, "dataprotection": False}
    for i in range(len(sys_args)):
        if sys_args[i] in project_setup.keys():
            return_dict[project_setup[sys_args[i]]] = sys_args[i+1]
    return return_dict
