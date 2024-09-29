"""
Program that prints asterisks based on password length
"""

MINIMUM_LENGTH_THRESHOLD = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH_THRESHOLD:
        print("Password must be at least 6 characters!")
        password = input("Password: ")
    return password


main()
