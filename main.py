from src.password_validator import validate_password
import math

password = input("Enter password: ")

if validate_password(password):
    print("Password is valid, small update")
else:
    print("Password is invalid, small update")
