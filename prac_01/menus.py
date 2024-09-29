"""
Program that features a series of menu options for a user to select
"""

name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    menu_choice = input(">>> ").upper()
print("Finished.")
