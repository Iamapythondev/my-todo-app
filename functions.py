FILEPATH = r"files\todos.txt"

def get_todos(filepath=FILEPATH):
    """ this function is to read the list from the file mentioned in the parameter """
    with open(filepath, 'r') as file_local:
        todos_list = file_local.readlines()
    return todos_list


def write_todos(todos_arg, filepath=FILEPATH):
    """ write a todo item to list in a file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return

if __name__ == "__main__":
    print(get_todos())