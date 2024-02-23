# dict2.py
# program that reads in student info in a dict and 
#   prints out the data.
# author: eoghan walsh

student_name = str(input("Please enter your name: "))
course_name = str(input("Please enter course name: "))
grade = int(input("Please enter course grade: "))

student = {
    "Name" : student_name,
    "Courses" : [
        {
            "Course_Name" : course_name,
            "Grade" : grade
        }
    ]
}

print(f"Name: {student['Name']}")

for course in student['Courses']:
    print(f"\t{course['Course_Name']}: {course['Grade']}")