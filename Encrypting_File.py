#!/usr/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import sys

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print(f"Usage: ./Encrypting_File.py [File_Name] [Public_Key.pem]\n")
    print(f"OPTIONAL: ./Encrypting_File.py [File_Name] [Public_Key.pem] [Encrypted_File_Name]\n\n"
          f"ATTENTION!!!\nBy default, the original file will be OVERWRITTEN by the encrypted file")
    exit(1)

with open(sys.argv[1], "rb") as data_file:
    data_tobe_encrypted = data_file.read()

public_pem = sys.argv[2]    # Loading the public key into memory.

# Deserializing the Public Key.
with open(public_pem, "rb") as public_pem_file:
    public_key = serialization.load_pem_public_key(public_pem_file.read())

# Encrypting the data:
encrypted_data = public_key.encrypt(
    plaintext=data_tobe_encrypted,

    # Padding is a way, used in encryption, to extend the cipher text, so it will match the block size of the hash.
    padding=padding.OAEP(   # OAEP (Optimal Asymmetric Encryption Padding) is recommended for RSA encryption.

        # MFG (Mask Generation Function) will create a mask with the same size of the inputted data.
        mgf=padding.MGF1(algorithm=hashes.SHA256()),

        # SHA256 is a hashing algorithm used to create hashes. In this case, a hash is used to authenticate the message,
        # making sure the data is unaltered, therefore, it's reliable.
        algorithm=hashes.SHA256(),
        label=None
    )
)

try:
    if sys.argv[3]:
        filename = sys.argv[1].split(".")
        file_new_name = f"{sys.argv[3]}.{filename[1]}"

        with open(file_new_name, "wb") as file:
            file.write(encrypted_data)

except IndexError:

    with open(sys.argv[1], "wb") as file:
        file.write(encrypted_data)
