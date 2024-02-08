# div.py
# dividing one number by another
# author: eoghan walsh

number1 = int(input("Enter first number: "))
number2 = int(input("Enter the number you want to divide by: "))
i = number1 // number2
r = number1 % number2
print(f"{number1} divided by {number2} is {i} with remainder {r}")