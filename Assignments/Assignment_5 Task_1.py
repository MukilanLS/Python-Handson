name_marks = {"Alice":85, "Alexa":98, "Bob":45, "Murali":34}

# User Input
student_name = input("Enter the student's name: ")

# Checking the Student name is present in dictionary
if student_name in name_marks:
    print(f"{student_name}'s marks:", name_marks[student_name])
else:
    print(student_name, "not found")