"""Estimate: 2.5 hours"""

from project import Project
from datetime import datetime


FILENAME = "projects.txt"


def main():
    """Main menu-driven project manager."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    print(MENU)

    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").lower()

    if input(f"Would you like to save to {FILENAME}? ").lower() in ['yes', 'y']:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects: ")
    for p in incomplete:
        print(f"  {p}")

    print("Completed projects: ")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Filter projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.starts_after(filter_date)], key=lambda p: p.start_date)

    for p in filtered:
        print(p)


def add_new_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    new_project = Project(name, start_date_str, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (IndexError, ValueError):
        print("Invalid project choice")
        return

    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


if __name__ == '__main__':
    main()
