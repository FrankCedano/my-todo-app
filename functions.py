FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """" Read a text file and returns the
    to-do items.
    """
    with open(filepath, "r") as local_file:
        """ Write the to-do items to the todo file."""
        local_todos = local_file.readlines()
        return local_todos
#print(help(get_todos))
def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())