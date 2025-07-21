"""Estimate: 1.5 hours"""

from datetime import datetime


class Project:
    """Represent a single project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority (for sorting)."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is completed (100%)."""
        return self.completion_percentage == 100

    def starts_after(self, date):
        """Return True if project starts after given date."""
        return self.start_date > date
