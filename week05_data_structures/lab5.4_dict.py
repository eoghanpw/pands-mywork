# dict.py
# program that stores student info in a dict and 
#   prints out the data.
# author: eoghan walsh

student = {
    "Name" : "Mary",
    "Courses" : [
        {
            "Course_Name" : "Programming",
            "Grade" : 45
        },
        {
            "Course_Name" : "History",
            "Grade" : 99
        }
    ]
}

print(f"Name: {student['Name']}")

for course in student['Courses']:
    print(f"\t{course['Course_Name']}: {course['Grade']}")