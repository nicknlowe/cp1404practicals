"""
Program to determine score status and print stars based on inputted score
"""

MENU = """G - Input score
P - Get status result
S - View stars
Q - Quit program"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thanks for using the program")


def print_stars(score):
    for i in range(int(score)):
        print("*", end="")
    print()


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Input a valid score")
        score = float(input("Enter score: "))
    return score


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"


main()
