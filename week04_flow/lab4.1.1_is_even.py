# is_even.py
# this program reads in a number and tells user
# if even or odd
# author: eoghan walsh

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")