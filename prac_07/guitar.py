"""
CP1404/CP5632 Practical
Guitar class
"""

CURRENT_YEAR = 2024
VINTAGE_AGE_THRESHOLD = 50


class Guitar:
    """Represent the details for a Guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar instance string."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return if the guitar object is younger than another instance."""
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE_THRESHOLD
