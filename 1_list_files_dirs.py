
import os

def list_contents(path):
    only_dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    only_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_contents = os.listdir(path)
    return only_dirs, only_files, all_contents
