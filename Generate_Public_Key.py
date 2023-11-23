from cryptography.hazmat.primitives import serialization
from Generate_Private_Key import private_key

# Generating a Public Key. To create a public key that will be used to encrypt files, the public key needs to be
# generated as an instance of a private key, so the private one can decrypt the file encrypted by the public.
public_key = private_key.public_key()

# Serializing the Public Key.
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open(f"Public.pem", "wb") as public_pem_file:
    public_pem_file.write(public_pem)
