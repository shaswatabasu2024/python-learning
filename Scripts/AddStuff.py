stuff = ["one", "two", "three", "four", "five"] # list for which items can be added, removed, cleared and displayed.

command = "" # empty string for command.

while command != "quit": # a while loop that runs until the user types quit.
    command = input("> ").lower() # updates the command variable with the user input.
    if command == "list": # if this command is called the list is displayed.
        for item in stuff:
            print(item)
    elif command == "add": # if this command is called an item is added to the list.
        item = input("Item: ")
        where_to = int(input("Where to add: "))
        stuff.insert(where_to, item)
    elif command == "remove": # if this command is called an item is removed from the list.
        item = input("Item: ")
        if item in stuff:
            stuff.remove(item)
    elif command == "clear": # if this command is called the list is cleared.
        stuff.clear()