# messing with files
# author: eoghan walsh

'''
FILENAME = "data.txt"

with open(FILENAME, 'rt') as f:
    for data in f:
        print(data.strip())

FILENAME = "test.txt"
with open(FILENAME, 'wt') as f:
    f.write("Hello world")
    

FILENAME = "test.txt"
with open(FILENAME) as f:
    str = f.read()
    print(str)

with open ('test.txt', 'rt') as f:
    for line in f:
        print(line)

with open('test.txt', 'w+t') as f:
    for lie in f:
        print(line)

import os
os.remove('test.txt')

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, "already exists")
else:
    print(filename, "does not exist")

import json

electric_bill = {
    "name": "Andrew",
    "amount": "99"
}
with open("store_data.json", "wt") as f:
    json.dump(electric_bill, f)

FILENAME = "store_data.json"
with open(FILENAME, "rt") as file:
    for line in file:
        print(line,end=" ")

with open("store_data.json", "rt") as f:
    read_dict = json.load(f)
    print(read_dict["amount"])


FILENAME = "data.csv"
with open(FILENAME, "rt") as file:
    for line in file:
        print (line, end='')

FILENAME="data.csv"
with open(FILENAME, "rt") as file:
    csvReader = csv.reader(file, delimiter = ',')
    for line in csvReader:
        age = line[2]
        print(age)


FILENAME = "data.csv"
with open(FILENAME, "rt") as file:
    csv_reader = csv.reader(file, delimiter = ",")
'''

import csv

my_dict = [
    {"first": "Andrew", "last": "Beatty", "age": "2"},
    {"first": "Eoghan", "last": "Walsh", "age": "22"},
    {"first": "John", "last": "Ahern", "age": "12"}
    ]

fieldnames = ["first", "last", "age"]

with open("data.csv", "w", newline = "") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    for dict_row in my_dict:
        writer.writerow(dict_row)
        print(dict_row)