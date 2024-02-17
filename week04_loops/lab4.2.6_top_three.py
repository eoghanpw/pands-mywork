# top_three.py
# program generates and prints 10 random numbers (0 to 100), 
#   and also prints the 3 highest numbers.
# authur: eoghan walsh

import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers = []

while len(numbers) < 10:
    numbers.append(random.randint(range_from,range_to))
    
print(f"10 random numbers are: {numbers}")

numbers.sort(reverse=True)

print(f"The highest {top_how_many} numbers are: {numbers[0:3]}")