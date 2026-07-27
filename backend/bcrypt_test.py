import bcrypt

password = b"CloudSense123"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

print(bcrypt.checkpw(password, hashed))