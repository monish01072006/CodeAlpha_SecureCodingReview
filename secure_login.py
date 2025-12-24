# Secure Login System
# Uses password hashing, validation, exception handling, and safer comparisons

import hashlib

stored_username = "admin"
stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

def validate_input(value, field):
    if not value.strip():
        print(f"{field} cannot be empty.")
        return False
    if not value.isalnum():
        print(f"{field} must contain only letters and numbers.")
        return False
    return True

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not validate_input(username, "Username"):
        exit()
    if not validate_input(password, "Password"):
        exit()

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and password_hash == stored_password_hash:
        print("Login successful")
    else:
        print("Invalid credentials")

except Exception:
    print("An error occurred while processing your request.")
