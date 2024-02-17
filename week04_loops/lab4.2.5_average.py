# average.py
# program that reads in numbers until user enters a 0.
#   the program then prints out the numbers and an average.
# author: eoghan walsh

numbers = []

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("Enter another number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers) / len(numbers))

print(f"The average is: {average}")