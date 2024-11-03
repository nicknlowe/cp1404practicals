"""
CP1404/CP5632 Practical
Store user emails and names in a dictionary
Estimate: 30 minutes
Actual:   26 minutes
"""


def main():
    """Create dictionary and prompt user for emails and names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        prompt = input(f"Is your name {name}? (Y/n) ")
        if prompt.upper() != "Y" and prompt != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
