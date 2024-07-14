while True:
    choice = input(
        "Would you like to create a student (cas) or find a student's information (fsi): "
    )
    if choice.lower() != "fsi" and choice.lower() != "cas":
        print("Invalid input please try a valid input like fsi or cas.")
        break
    student_id = input("Enter student id: ")
    if choice.lower() == "cas":
        student_exists = False
        with open("student_info.txt", "a+") as file:
            for line in file:
                if student_id in line:
                    print("Student id already exists.")
                    student_exists = True
                    break
            if not student_exists:
                student_name = input("Enter student name: ")

                student_age = input("Enter student age: ")

                student_year_born = input("Enter student's date of birth: ")

                with open("student_info.txt", "a") as file:
                    file.write("\n" + student_name + " Id: " + student_id +
                               " Age: " + student_age + " Date of birth: " +
                               student_year_born)

                print("Student information has been saved to student_info.txt")

    if choice.lower() == "fsi":
        is_student_exist = False
        with open("student_info.txt", "r") as file:
            for line in file:
                if student_id in line:
                    print(line)
                    is_student_exist = True
            if is_student_exist is not True:
                print("Student id does not exist.")