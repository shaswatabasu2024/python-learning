command = "" # first its value is blank

while command != "quit": # then we check if the value is not equal to quit
    command = input("> ").lower() # then we give the command a new value
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("You can start the car by typing 'start', stop the car by typing 'stop' or quit the game by typing 'quit'")
    elif command == "quit":
        print('''
        Thank you for playing!
        Your feedback is very important to us.
        So please feel free to leave us any feedback you have about the game.
        ''')
        break
    else:
        print("Sorry, I don't understand that...")