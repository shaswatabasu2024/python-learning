message = input("Enter message: ")

words = message.split()

emojis = {
    ":)": "😀",
    "(:": "😀",
    ":(": "😔",
    "):": "😔"
}

output = ""  # append oputput(append)

for word in words:
    output += emojis.get(word, word) + " "

print(output)