"""
Program that prints asterisks based on password length
"""

MINIMUM_LENGTH_THRESHOLD = 6

password = input("Password: ")
while len(password) < MINIMUM_LENGTH_THRESHOLD:
    print("Password must be at least 6 characters!")
    password = input("Password: ")
for i in range(len(password)):
    print("*", end="")
