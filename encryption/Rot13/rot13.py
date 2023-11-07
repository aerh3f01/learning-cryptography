# Rot13 is similar to Caesar Cipher, but it uses a fixed key of 13.


# makestrans is a function that creates a translation table
# allowing to set a mapping between two characters
# it takes two arguments: the first is a string of characters to be replaced
# the second is a string of characters to replace with

rot13translation = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
# since the translation is always 13 characters
# the strings can be pre-defined

def rot13(text):
    return text.translate(rot13translation)
    # translate() is a string method that returns a copy of the string
    # where all characters have been mapped through the translation table

if __name__ == '__main__':
    message = input("Enter message: ")
    print("Encrypted message: ", rot13(message))

# This is a simple encryption method that can be easily broken