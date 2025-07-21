"""
CP1404 - Practical
More Guitars! Load, display, sort and save guitars
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to load, sort, display and update guitars."""
    guitars = load_guitars(FILENAME)

    print("These are the guitars:")
    display_guitars(guitars)

    # Add new guitars
    guitars += get_user_guitars()

    # Sort by year
    guitars.sort()

    print("\nThese are the sorted guitars:")
    display_guitars(guitars)

    # Save updated list
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a numbered list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_user_guitars():
    """Prompt the user to enter new guitars."""
    print("\nEnter your new guitars (blank name to stop):")
    new_guitars = []
    name = input("Name: ").strip()
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost:,.2f} added.\n")
        except ValueError:
            print("Invalid input. Please enter correct values.")
        name = input("Name: ").strip()
    return new_guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == '__main__':
    main()
