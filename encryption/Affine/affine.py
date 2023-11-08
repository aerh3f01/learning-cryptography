# The Affine Cipher is a combination of the Caesar Cipher and Multiplicative Cipher.

# The basic encryption algorithm is:
# E(x) = (ax + b) mod m
# where m is the size of the alphabet
# a and b are the keys of the cipher

# The value of a must be a co-prime of m
# (must have no common factors other than 1)
# Since the English alphabet has 26 letters, m = 26
# Therefore the co-primes of 26 are [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

import random

class Affine():
    key_a = 0
    key_b = 0
    modulus_m = 26
    a_options = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    
    def __init__(self):
        pass

    def encryptChar(self, char):
        if char.isupper():
            return chr((self.key_a * (ord(char) - 65) + self.key_b) % self.modulus_m + 65)
        else:
            return chr((self.key_a * (ord(char) - 97) + self.key_b) % self.modulus_m + 97)
        
    def encrypt(self, message):
        return "".join(map(self.encryptChar, message))
    
    def getMessage(self):
        message = input("Enter message: ")
        return message

    def getKey(self):
        self.key_a = random.choice(self.a_options)
        self.key_b = random.randint(0, 25)
        print("Key A: ", self.key_a)
        print("Key B: ", self.key_b)

if __name__ == '__main__':
    affine = Affine()
    affine.getKey()
    message = affine.getMessage()
    print("Encrypted message: ", affine.encrypt(message))