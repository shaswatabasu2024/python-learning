# 1 - 40 any number divisible by 3 you have to write Fizz and 5 you have to write Buzz if both then FizzBuzz

for number in range(1, 41):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)