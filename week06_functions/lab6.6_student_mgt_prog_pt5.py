# student management program part 6
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
def do_add(students):
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = read_modules()
    students.append(current_student)

# function 3 - adding modules
def read_modules():
    modules = []
    module_name = input("Enter the first Module name (blank to quit): ")
    while module_name != "":
        module = {}
        module["name"] = module_name
        module["grade"] = int(input("Enter grade: "))
        modules.append(module)
        module_name = input("Enter next module name (blank to quit): ")
    return modules

# function 5 - display modules
def display_modules(modules):
    print("\tName   \t\tGrade")
    for module in modules:
        print(f"\t{module['name']}   \t\t{module['grade']}")

# function 4 - viewing student
def do_view(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

# main program
students = []
choice = user_menu()
while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print("\nPlease select either a, v or q\n")
    choice = user_menu()