filepath = 'files/todos.txt'


def get_todos(path=filepath) -> list:
    """" Get data from file and return the list"""
    with open(path, 'r') as file:
        todos_arg = file.readlines()
    return todos_arg


def write_todos(todos_arg, path=filepath):
    """ Write data-list to file"""
    with open(path, 'w') as file:
        file.writelines(todos_arg)
