"""
CP1404/CP5632 Practical
Project class
"""


class Project:
    """Represent information about a Project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string of a Project instance."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}"
                f", completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return if a Project priority is smaller than another instance."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if a Project has been completed."""
        return self.completion_percentage == 100
