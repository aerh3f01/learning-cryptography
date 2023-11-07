# Learning basic hacking techniques against caeser ciphers
# This is a brute force attack against a caeser cipher
# It will try every possible shift and print the result
def caeser_hack(message):
    text = ""
    for shift in range(26):
        for i in range(len(message)):
            char = message[i]
            if char.isupper():
                text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                text += chr((ord(char) + shift - 97) % 26 + 97)
        print("Shift: %s, Message: %s " % (shift, text))
        text = ""


if __name__ == '__main__':
    message = input("Enter message: ")
    caeser_hack(message)
