# grade.py
# this program reads in a student's percentage mark and 
# prints out corresponding grade.
# author: eoghan walsh

mark = float(input("Please enter you mark out of 100: "))

if (mark < 0) or (mark > 100):
    print("Invalid mark")

elif (mark < 40):
    print("Fail")

elif (mark < 50):
    print("Pass")

elif (mark < 60):
    print("Merit 2")

elif (mark < 70):
    print("Merit 1")

elif (mark >= 70):
    print("Distinction")