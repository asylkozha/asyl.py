
def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())
