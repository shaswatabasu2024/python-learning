def emojify(Input):
    words = Input.split()  # split Input into a list

    emojis = {
        ":)": "😀",
        "(:": "😀",
        ":(": "😔",
        "):": "😔"
    }  # created dictionary for emojis

    output = ""  # append emojis/words to output

    for word in words:  # gets each word in the list
        output += emojis.get(word, word) + " "  # if word is in the dictionary, it becomes an emoji else it gives the

    return output


message = input("Enter Input: ")  # enter user Input

print(emojify(message))
