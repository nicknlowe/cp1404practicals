"""
CP1404/CP5632 Practical
Client code for the Guitar class
"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read and display guitars from oldest to youngest."""
    guitars = []
    read_file(FILENAME, guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_file(filename, guitars):
    """Read guitar data from a CSV file."""
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()
