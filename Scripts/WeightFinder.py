weight = input("Enter your weight: ")

weight_find = input("Is your weight in pounds (P) or kilograms (K)? ")

if weight_find.upper() == "P":
    kilograms = float(weight) * 0.45359237
    print("Your weight in kilograms is: " + str(kilograms))

elif weight_find.upper() == "K":
    pounds = float(weight) * 2.20462262
    print("Your weight in pounds is: " + str(pounds))
else:
    print("Invalid input")