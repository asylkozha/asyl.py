
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is file {letter}.txt")
