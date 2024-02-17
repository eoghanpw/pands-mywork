# guess1.py
# program that prompts user to guess a number until
# the user guesses the correct one.
# author: eoghan walsh

correct_num = 30
guess_num = int(input("Please guess a number: "))

while guess_num != correct_num:
    print("Wrong")
    guess_num = int(input("Please guess again: "))

print(f"Well done! The number was {correct_num}")