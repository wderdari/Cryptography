from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, load_pem_parameters, \
    load_pem_public_key, load_pem_private_key


# 1. Generate private key x using the PEM encoding.
# 2. Generate private key y using the PEM encoding.
# 3. Calculate a public key A & B
# 4. Compute the key K = (Y_B)^(X_A) mod q
# 5. Compute the other key using K = (Y_A)^(X_B) mod q

def Diffie_Hellman():

    # Shared information provided by KEYS.txt - contains DF parameters and public key
    pem_data = b'-----BEGIN DH PARAMETERS----- \nMEYCQQDP+dSNnBRy4jbHTvr0YcEk0bMzisMy+p/k9VYCb+gPNU/OSDkmEX62YKTc\nj1QrA o8+f3du/bjdfVKfv71LWtxjAgEC\n-----END DH PARAMETERS-----\n'
    public_key_data = b'-----BEGIN PUBLIC KEY-----\nMIGaMFMGCSqGSIb3DQEDATBGAkEAz/nUjZwUcuI2x0769GHBJNGzM4rDMvqf5PVW\nAm/oDzVPzkg5JhF+tmCk3I9UKwKPPn93bv243X1Sn7+9S1rcYwIBAgNDAAJAYyRw\n2K7KvbqudRx9DQtKH/tAQjDtDMIw7hFWYslMFnE/t44wArXQ/wuo0NPhFL4b63R8\nJZA7cF7tP+CAj3WHFA==\n-----END PUBLIC KEY-----\n'

    dh_paramaters = load_pem_parameters(pem_data)

    private_key = dh_paramaters.generate_private_key()  # Generate private key from the given DH parameter.

    public_key_a = private_key.public_key()  # Public key that will be returned in PEM format.

    public_key_b = load_pem_public_key(public_key_data) # Load provided public key.

    shared_key = private_key.exchange(public_key_b) # Key exchanged carried out and shared key is returned.

    derived_key = HKDF(hashes.SHA256(), 32, None, b'handshake data').derive(shared_key)  # HMAC-based E&E key derivation. Returns bytes.

    public_key_pem = public_key_a.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)  # Encodes the public key into PEM.

    return public_key_pem, derived_key


if __name__ == '__main__':
    print(Diffie_Hellman())
