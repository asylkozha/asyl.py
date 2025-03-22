
def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")
