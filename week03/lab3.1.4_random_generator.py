# random_generator.py
# program that prints out a random number between 1 and 10
# author: eoghan walsh

import random

print("Please select a range for the random number generator.")
number1 = int(input("From number: "))
number2 = int(input("To number: "))
answer = random.randint(number1,number2)
print(f"Here is a random number: {answer}")