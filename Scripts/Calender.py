just_a_normal_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

user_input = ""

while user_input != "stop":
    user_input = input("What would you like to add, remove, or check on your list if you want to close the program type 'stop'? ").lower()

    if user_input == "stop":
        break


    elif user_input == "check":
        print(just_a_normal_day)
    elif user_input == "add":
        user_input = input("What would you like to add? ")
        user_input_where = input("Which index would you like to store it at? ")
        just_a_normal_day.insert(int(user_input_where), user_input)

    elif user_input == "remove":
        user_input = input("What would you like to remove? ")
        just_a_normal_day.remove(user_input)
        print(just_a_normal_day)

    else:
        print("Invalid Input please try using the words 'add', 'check', 'remove', or 'stop'")

