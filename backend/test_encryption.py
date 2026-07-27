from app.cloud.encryption import encrypt, decrypt

secret = "MySecretKey123"

encrypted = encrypt(secret)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted:", decrypted)