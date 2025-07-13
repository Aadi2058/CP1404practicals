"""
CP1404/CP5632 Practical - Guitar class tests
Estimate: 10 minutes
Actual: 6 minutes
"""

from guitar import Guitar

def main():
    """Test the Guitar class methods."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500.00)

    print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")


main()
