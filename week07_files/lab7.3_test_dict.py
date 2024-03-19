# test_dict.py
# function that will store a dict to a JSON file.
# author: eoghan walsh

import json

FILENAME = "test_dict.json"

sample = dict(name ="fred", age = 31, grades = [1, 34, 55])

def write_dict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

write_dict(sample)