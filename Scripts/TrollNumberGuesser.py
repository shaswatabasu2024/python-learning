print("Welcome to the Number Guesser! This is a game where the program will guess your number! Totally legit!")

number = input("Enter your number (please make sure its a number and don't include any letters): ")

x = number

print(x)

if x == "123":
    gg = input("You have unlocked a special please say Yes if you want to continue and no if you want to exit: ")
    if gg.lower() == "yes":
        activation_number = input("To proceed enter your activation code: ")  # its 6969
        if activation_number == "6969":
            import random

            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            number_of_passwords = 0

            while number_of_passwords < 1:

                random.shuffle(numbers)

                number_of_passwords += 1

                output = ""

                for number in numbers:
                    output += str(number)
                    length = len(output)
                    if length > 3:
                        break

                user_guess = input("Enter your guess for what the random number might be: ")

                if user_guess == output:
                    user_name = input("Please enter your name: ")
                    print(user_name, "You guessed right! The number was " + output + "! You win!")
                    break
                else:
                    user_name_lose = input("Please enter your name: ")
                    print(user_name_lose, "You guessed wrong! The number was " + output + "! I am sorry. You lose.")
                    break
            else:
                print("Your activation code is incorrect!")
        elif gg.lower() == "no":
            print("Okay, see you next time!")
        else:
            print("Please enter yes or no next time!")
