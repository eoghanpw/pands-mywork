# floor.py
# program take a float number and outputs an integer rounded down
# author: eoghan walsh

import math

num_float = float(input("Enter a float number: "))
num_round = math.floor(num_float)
print(f"{num_float} rounded down is {num_round}")