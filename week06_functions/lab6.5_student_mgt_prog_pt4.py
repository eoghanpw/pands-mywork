# student management program part 4
# program allows user to create new students and 
#   to view new students
# author: eoghan walsh


students = []

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

read_modules()


