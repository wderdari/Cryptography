from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def findCiphertext():

    # Same key and IV are used. Use these as attack vectors. Message stream XOR Ciphertext Stream = Keystream
    # https://datatracker.ietf.org/doc/html/rfc3686.html

    message_a = b"I'll give you 500 and that's my last offer."
    message_b = b"I'll give you 100 and that's my last offer."

    ciphertext_a = b"\xef@\x92<$J\xb2\x8c\xbc\xabl'\x016\xd2{W-8\xcas\x83*\xa1\xef)\xc0\xda\x7fe\xab\xb1\x94\x7fJ\x98\xc8\xeei|'t\xb4"

    # Ciphertext XOR message = keystream. ciphertext_B given by XOR message_b
    keystream = bytes(a ^ b for a, b in zip(message_a, ciphertext_a))
    ciphertext_b = bytes(a ^ b for a, b in zip(message_b, keystream))

    return ciphertext_b


if __name__ == '__main__':
    print(findCiphertext())
