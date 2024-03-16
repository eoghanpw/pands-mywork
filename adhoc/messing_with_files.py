# messing with files
# author: eoghan walsh

FILENAME = "data.txt"

with open(FILENAME, 'rt') as f:
    for data in f:
        print(data.strip())