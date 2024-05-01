orgMsg = input("Please enter a sentence: ")
newMsg = ""

# iterate over the given message from user, assigning each character to the char variable.
for i in range(len(orgMsg)):
    char = orgMsg[i]
    # check if character is uppercase and encrypt accordingly.
    if (char.isupper()):
        newMsg += chr((ord(char) + 5-65) % 26 + 65)
    # check if character is a space so we do not encrypt.
    elif (char == " "):
        newMsg += char
    # check if character is anything other than alphanumeric or a space, aka a special character, and do not encrypt.
    elif not (char.isalpha() or char.isdigit() or char == " " ):
        newMsg += char
    # otherwise encrypt the rest of the message.
    else:
        newMsg += chr((ord(char) + 5-97) % 26 + 97)

# diplay to the user the encrypted message in lowercase format.    
print ("The encrypted sentence is: " + newMsg.lower())