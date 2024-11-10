"""
CP1404/CP5632 Practical
Programming Language class
"""


class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return Programming Language instance string."""
        return f"{self.name}: Typing - {self.typing}, Reflection - {self.reflection}, Released - {self.typing}"

    def is_dynamic(self):
        """Determine if a Programming Language is dynamically typed."""
        return self.typing == "Dynamic"
