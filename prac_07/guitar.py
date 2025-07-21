"""
CP1404 - Practical
Guitar class for storing guitar details
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Construct a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Define less than operator based on guitar's year."""
        return self.year < other.year

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age(2025) >= 50  # Assuming current year is 2025
