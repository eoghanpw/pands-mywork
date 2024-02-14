# rounded_grade.py
# this program reads in a student's percentage mark and 
# prints out corresponding grade.
# author: eoghan walsh

mark = float(input("Please enter you mark out of 100: "))

if (mark < 0) or (mark > 100):
    print("Invalid mark")

elif (mark < 39.5):
    print("Fail")

elif (mark < 49.5):
    print("Pass")

elif (mark < 59.5):
    print("Merit 2")

elif (mark < 69.5):
    print("Merit 1")

elif (mark >= 69.5):
    print("Distinction")