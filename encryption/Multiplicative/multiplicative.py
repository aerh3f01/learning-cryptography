# A multiplicative cipher uses a key that is a number between 0 and 25.
# This number is used to multiply the ASCII value of the plaintext character.

# base formula:
# (ASCII value * key)mod(number of alphabets)

# assuming all latters are upper case

def multiplicative(key, character):
    if character.isupper():
        return chr(((ord(character) - 65) * key) % 26 + 65)
    else:
        return chr(((ord(character) - 97) * key) % 26 + 97)

def encrypt(key, message):
    cipher = ""
    for character in message:
        cipher += multiplicative(key, character)
    return cipher

if __name__ == '__main__':
    message = input("Enter message (upper case): ")
    key = int(input("Enter key (0-25): "))
    print("Encrypted message: ", encrypt(key, message))