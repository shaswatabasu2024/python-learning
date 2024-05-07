# basic calculator

first_user_input = input("Enter the first number: ") # gets first Input/ calclation Input.

second_user_input = input("Enter the second number: ") # gets second Input/ calclation Input.

operation = input("Enter the operation ex: +, -, *, /, //, %, **: ") # gets the funky operation thingy required.

if operation == "+":
    print(float(first_user_input) + float(second_user_input)) # funky math claculations thingys.

elif operation == "-":
    print(float(first_user_input) - float(second_user_input))

elif operation == "*":
    print(float(first_user_input) * float(second_user_input))

elif operation == "/":
    print(float(first_user_input) / float(second_user_input))

elif operation == "//":
    print(float(first_user_input) // float(second_user_input)) # funky math claculations thingys that does not use decimal but I made it use decimals so pog

elif operation == "%":
    print(float(first_user_input) % float(second_user_input)) # pogger thing that only prints the remainder.

elif operation == "**":
    print(float(first_user_input) ** float(second_user_input)) # does the things with the exponents.

else:
    print("Unknown operation please try, +, -, *, /, //, %, **.") # if funky math operation thing is = bad then this prints.