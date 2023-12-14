import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for i in range(length))
    return secure_password

# Example usage:
password = generate_password(16)
print("Generated Password:", password)
