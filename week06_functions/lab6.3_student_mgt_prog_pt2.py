# student management program part 2
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

# function 2 - adding new student
def do_add():
    print("adding in")

# function 3 - viewing student

def do_view():
    print("viewing")

# main program

choice = user_menu()
while choice != "q":
    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice != "q":
        print("\nPlease select either a, v or q\n")
    choice = user_menu()