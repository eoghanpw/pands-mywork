# count
# author: eoghan walsh

import os.path

FILENAME = "count2.txt"

def write_number(number):
    with open(FILENAME,"wt") as f:
        f.write(str(number))

if not os.path.isfile(FILENAME):
    print("File does not exist")
    write_number(0)

def read_number():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0

num = read_number()
num +=1
print(f"We have run this program {num} times")
write_number(num)