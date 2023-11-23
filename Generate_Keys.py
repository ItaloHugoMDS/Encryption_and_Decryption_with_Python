#!/usr/bin/python3

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

if len(sys.argv) != 4:
    print("Usage: ./Generate_Keys.py [Name_of_Private_PEM] [Name_of_Public_PEM] [Private_Key_Password]")
    exit(1)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(bytes(f"{sys.argv[3]}", "utf-8"))
)

public_key = private_key.public_key()

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open(f"{sys.argv[1]}.pem", "wb") as private_pem_file:
    private_pem_file.write(private_pem)

with open(f"{sys.argv[2]}.pem", "wb") as public_pem_file:
    public_pem_file.write(public_pem)
