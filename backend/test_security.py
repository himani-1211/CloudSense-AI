from app.core.security import hash_password, verify_password

password = "CloudSense123"

hashed = hash_password(password)

print("Original:", password)
print("Hashed:", hashed)

print("Correct Password:", verify_password(password, hashed))
print("Wrong Password:", verify_password("abc123", hashed))