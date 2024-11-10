"""
CP1404/CP5632 Practical
Guitar class test program
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2024

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitar("Another Guitar", 2013, 250)

print(f"{first_guitar.name} get_age() - Expected 102. Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 11. Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True. Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is vintage() - Expected False. Got {second_guitar.is_vintage()}")
