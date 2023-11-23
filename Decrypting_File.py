#!/usr/bin/python3

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import sys

if len(sys.argv) < 4 or len(sys.argv) > 5:
    print(f"Usage: ./Decrypting_File.py [File_ToBe_Decrypted] [Private_Key.pem] [Private_Key_Password]\n")
    print(f"OPTIONAL: ./Decrypting_File.py [File_ToBe_Decrypted] [Private_Key.pem] [Private_Key_Password] "
          f"[Encrypted_File_Name]\n\n"
          f"ATTENTION!!!\nBy default, the original file will be OVERWRITTEN by the decrypted file")
    exit(1)

# Loading the encrypted data into memory.
with open(sys.argv[1], "rb") as file:
    encrypted_data = file.read()

private_pem = sys.argv[2]

# Deserializing the Private Key.
with open(private_pem, "rb") as private_pem_file:
    private_key = serialization.load_pem_private_key(
        data=private_pem_file.read(),
        password=bytes(f"{sys.argv[3]}", "utf-8")
    )

decrypted_data = private_key.decrypt(
    ciphertext=encrypted_data,
    padding=padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

try:
    if sys.argv[4]:
        filename = sys.argv[1].split(".")
        file_new_name = f"{sys.argv[4]}.{filename[1]}"

        with open(file_new_name, "wb") as file:
            file.write(decrypted_data)

except IndexError:

    with open(sys.argv[1], "wb") as file:
        file.write(decrypted_data)
