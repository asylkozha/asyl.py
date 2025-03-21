text = str(input())
upp = sum(map(str.isupper , text))
loww = sum(map(str.islower , text))
print(f"uppercase: {upp},Lowercase: {loww}")