
def copy_file(source, destination):
    with open(source, 'r') as src:
        content = src.read()
    with open(destination, 'w') as dest:
        dest.write(content)
