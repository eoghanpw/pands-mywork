# student management program part 7
# program allows user to create, view and  
#   save new students
# author: eoghan walsh

import json

students = []

FILENAME = "student_data.json"

def write_dict(obj):
    with open(FILENAME,'wt') as f:
        json.dump(obj,f)

def read_dict():
    with open(FILENAME) as f:
        return json.load(f)

# function 1 - display menu for user input
def user_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) Load students")    
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ")
    return choice

# function 2 - adding new student
def do_add():
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
def do_view():
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

# function 5 - save student
def do_save():
    write_dict(students)
    print("students saved")

# function 6 - load students
def do_load():
    global students
    students = read_dict()
    print("students loaded")

# main program
choice = user_menu()
while choice != "q":
    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice == "l":
        do_load()
    elif choice == "s":
        do_save()
    elif choice != "q":
        print("\nPlease select either a, v or q\n")
    choice = user_menu()