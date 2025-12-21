# Insecure Login System
# This code contains security vulnerabilities

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid credentials")
