# Creating a basic Caesar Cipher in Python
# A Caesar Cipher is a simple substitution cipher where one letter is replaced by another.
# Also known as a shift cipher, the Caesar Cipher is one of the oldest and simplest ciphers.

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            # chr() converts an ascii integer to a character
            # ord() converts a character to an ascii integer
            # 65 is the ascii integer for 'A'
            
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
            # like above, but for lowercase letters
            # 97 is the ascii integer for 'a'
    return result

if __name__ == '__main__':
    message = input("Enter message: ")
    shift = int(input("Enter shift number: "))
    print("Encrypted message: ", encrypt(message, shift))

