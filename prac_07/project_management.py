"""
CP1404/CP5632 Practical
Project Management Program that features the Project class
"""

from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter by date
- (A)dd new project
- (U)pdate project"""


def main():
    projects = read_file(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Please select a valid option!")
        print(MENU)
        choice = input(">>> ").upper()


def read_file(filename):
    """Read project data from a text file and convert instances into a list."""
    projects = []
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


main()
