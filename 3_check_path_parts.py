
import os

def path_info(path):
    if os.path.exists(path):
        return {
            "filename": os.path.basename(path),
            "directory": os.path.dirname(path)
        }
    return None
