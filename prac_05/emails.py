"""
CP1404/CP5632 Practical
Store user emails and names in a dictionary
Estimate: 30 minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()

    prompt = input(f"Is your name {name}? (Y/n) ")
    if prompt.upper() != "Y" and prompt != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
