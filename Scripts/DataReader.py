user_assignment = input("Enter assignment number: ")

with open("data.txt", "r") as file:
    students = file.readlines()
    for student in students:
        if student.find(user_assignment) != -1:
            print(student)
