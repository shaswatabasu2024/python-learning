import StudentClass

services = input("Would you like to register a student (yes/no): ")

are_you_sure = input("Are you sure you want to register a student (yes/no): ")

list_of_students = []

while are_you_sure == "yes":
    name = input("Enter student's name: ")
    last_name = input("Enter student's last name: ")
    age = input("Enter student's age: ")
    list_of_students.append(StudentClass.Student(name, last_name, age))
    save = input("Would you like to save your student info or write more? (yes/no): ")
    if save == "yes":
        for student in list_of_students:
            print(student.name, student.last_name, student.age)
        # Using open() function
        file_path = "data.txt"

        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write content to the file
            for student in list_of_students:
                file.write(student.name + " " + student.last_name + " " + student.age + "\n")

        print(f"File '{file_path}' created successfully.")
