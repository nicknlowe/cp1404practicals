"""
CP1404/CP5632 Practical
Project Management Program that features the Project class

Incomplete - started too late
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
    projects = load_file(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("Enter filename:")
            filename = input(">>> ").upper()
            projects = load_file(filename)
            if projects:
                print(f"Loaded {len(projects)} projects from {filename}")
            else:
                print("Invalid filename!")
        elif choice == "S":
            pass
        elif choice == "D":
            if projects:
                print("Incomplete projects:")
                display_incomplete_projects(projects)
                print("Completed projects:")
                display_complete_projects(projects)
            else:
                print("No projects to show!")
        elif choice == "F":
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filtered_projects_by_date = filter_projects_by_date(date, projects)
            display_incomplete_projects(filtered_projects_by_date)
            display_complete_projects(filtered_projects_by_date)
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Please select a valid option!")
        print(MENU)
        choice = input(">>> ").upper()


def load_file(filename):
    """Read project data from a text file and load instances into a list."""
    projects = []
    try:
        with open(filename, 'r', encoding='utf-8-sig') as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
                project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
    except FileNotFoundError:
        pass
    return projects


def display_incomplete_projects(projects):
    """Display all incomplete projects."""
    projects.sort()
    for project in projects:
        if not project.is_complete():
            print(project)


def display_complete_projects(projects):
    """Display all complete projects."""
    projects.sort()
    for project in projects:
        if project.is_complete():
            print(project)


def get_valid_date(prompt):
    """Get a valid date."""
    is_valid_date = False
    while not is_valid_date:
        date = input(prompt)
        try:
            valid_date = datetime.strptime(date, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date! Make sure the format is dd/mm/yyyy.")
    return valid_date


def filter_projects_by_date(date, projects):
    """Filter projects by a given date."""
    filtered_projects_by_date = [project for project in projects if project.start_date > date]
    return filtered_projects_by_date


main()
