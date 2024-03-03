# student management program part 1
# program allows user to create new students and 
#   to view new students
# author: eoghan walsh

# function 1 - display menu for user input
def user_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ")
    return choice

# main program

choice = user_menu()
print(f"You chose {choice}")