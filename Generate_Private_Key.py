from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

# Creating a Private Key
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Exponent use to decode the original value.
    key_size=2048   # Numbers of bits used in the key itself.
)

# print(private_key)

# Serializing the Private Key. Serialization is the process of turning the code object into a file for later use. The
# extension used for storing the private key is PEM (Privacy Enhanced Email), which is a format used for exchange
# certificates and keys.
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(bytes(f"123", "utf-8"))
)

# print(private_pem)

with open(f"Private.pem", "wb") as private_pem_file:
    private_pem_file.write(private_pem)
