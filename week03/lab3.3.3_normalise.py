# normalise.py
# program reads in a string and strips any leading or trailing spaces and converts to lower case
# author: eoghan walsh
# ref: https://www.w3schools.com/python/python_strings_modify.asp

string = input("Please enter a string: ")
norm_string = string.strip().lower()
input_length = len(string)
output_length = len(norm_string)
print(f"That string normalised is: {norm_string}")
print(f"We reduced the input string from {input_length} to {output_length} characters.")