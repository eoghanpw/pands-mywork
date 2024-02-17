# guess2.py
# program that prompts user to guess a number until
# the user guesses the correct one, while also telling
# the user if each guess if too high or too low.
# author: eoghan walsh

correct_num = 30
guess_num = int(input("Please guess a number: "))

while guess_num != correct_num:
    if guess_num < correct_num:
        print("Too low")

    else:
        print("Too high")

    guess_num = int(input("Please guess again: "))

print(f"Well done! The number was {correct_num}")