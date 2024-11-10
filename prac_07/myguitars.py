"""
CP1404/CP5632 Practical
Client code for the Guitar class
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read and display guitars from oldest to youngest."""
    guitars = []
    with open(FILENAME, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
