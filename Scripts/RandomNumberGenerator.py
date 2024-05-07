import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e", "f", "@", "h", "i", "j", "k", "l", "m", "n", "o",
           "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

number_of_passwords = 0

user_input_number_of_characters = int(input("Enter the number of characters: "))

while number_of_passwords < 10:

    random.shuffle(numbers)

    number_of_passwords += 1

    output = ""

    for number in numbers:
        output += str(number)
        length = len(output)
        if length > user_input_number_of_characters:
            break

    print(output)
