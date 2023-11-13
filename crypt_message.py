from cryptography.fernet import Fernet

message = "Hello World"

key = Fernet.generate_key()

fernet = Fernet(key)

enc_msg = fernet.encrypt(message.encode())
de_msg = fernet.decrypt(enc_msg).decode()

print("Original text: ", message)
print("Encoded text: ", enc_msg)
print("Decoded text: ",de_msg)
