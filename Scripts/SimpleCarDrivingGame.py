command = ""

started = False

stopped = False

while True:
    command = input("> ").lower()
    if command == "help":
        print('''
Start - to start the car
Stop - to stop the car
quit - to quit the game
        ''')
    elif command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            stopped = False
            print("Car started...")
    elif command == "stop":
        if stopped:
            print("Car already stopped.")
        else:
            stopped = True
            started = False
            print("Car stopped...")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")