"""
CP1404/CP5632 Practical
Email to name dictionary program

Estimated time: 25 minutes
Actual time: 30 minutes
"""

def extract_name(email):
    """Extract and format name from email address."""
    name = email.split('@')[0].replace('.', ' ').replace('-', ' ').title()
    return name

# Dictionary to store email to name mappings
email_to_name = {}

# Input loop for emails
email = input("Email: ")
while email != "":
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").lower() or 'y'
    if confirmation != 'y':
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

# Print all email-name pairs
for email, name in email_to_name.items():
    print(f"{name} ({email})")