# Required imports
import string


def encryptAffine(plaintext, a, b):


    charcipher = {} # Dictionary to store each plain text character's corresponding cipher character.

    # Converts every letter of the alphabet to it's corresponsing cipher and stores it into the dictionary.
    for i in range(26):
        plain_chr = string.ascii_uppercase[i]
        x = ord(plain_chr) - ord('A')  # Subtract A to get character's position in the alphabet.
        cipher_chr = string.ascii_uppercase[((a * x + b) % 26)]  # Apply formula to the character.
        charcipher[plain_chr] = cipher_chr  # Add to position i in dictionary (starts from 0 up to 26)

    ciphertext = ""

    for i in plaintext:
        if i in charcipher:
            ciphertext += charcipher[i]  # Checks to see if plain text character is in the dictionary. Handles non-uppercase characters.
        else:
            ciphertext += i  #  Non-uppercase characters are not converted to their value in the cipher dictionary.

    return ciphertext


if __name__ == '__main__':
    print(encryptAffine("He!!0 w0R!4", 123, 500))

# if plainchar.islower():
#            ciphertext = ciphertext + plainchar
#
#
#        if plainchar == " ":
#            ciphertext = ciphertext + " "  # Includes a space in the ciphertext according to the plaintext


 # if i.isupper() & i.isalpha():
 #            x = ord(i) - 65  # ord() converts letter to ASCII value. Subtract 67 for alphabet position.
 #            if x == 26:
 #                x = 0
 #            ciphertext = ciphertext + (chr(((a * ord(i) + b) % 26) + 67))  # Uses the affine function to encrypt
 #
 #        else:
 #            ciphertext = ciphertext + i