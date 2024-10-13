"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_data(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_data(data):
    """Display data in a readable format."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:3} students")


main()
