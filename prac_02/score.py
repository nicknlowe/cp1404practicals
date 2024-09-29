"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))


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
