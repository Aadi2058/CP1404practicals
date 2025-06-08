"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
"""

# Basic examples
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# 1. Manual concatenation (not recommended)
print("My guitar: " + name + ", first made in " + str(year))

# 2. Using str.format() (older method)
print("My guitar: {}, first made in {}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# 3. f-string formatting (modern, preferred)
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency
print("My {} would cost ${:,.2f}".format(name, cost))  # str.format version
print(f"My {name} would cost ${cost:,.2f}")  # f-string version

# Alignment and column formatting
numbers = [1, 19, 123, 456, -25]
print("\nAlignment examples:")
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")  # Right-aligned in 5 spaces

# ===== TODO SOLUTIONS =====

# Task 1: Format guitar information
print(f"\n{year} {name} for about ${cost:,.0f}!")

# Task 2: Powers of 2 with right-aligned columns
print("\nPowers of 2:")
for exponent in range(0, 11):
    print(f"2 ^{exponent:2} is {2 ** exponent:4}")

# ===== ADDITIONAL FORMATTING EXAMPLES =====

# Number formatting examples
value = 12345.6789
print("\nNumber formatting examples:")
print(f"Default: {value}")
print(f"2 decimal places: {value:.2f}")
print(f"With commas: {value:,.2f}")
print(f"Right-aligned 15 width: {value:15,.2f}")
print(f"Left-aligned 15 width: {value:<15,.2f}")
print(f"Centered 15 width: {value:^15,.2f}")
print(f"Zero-padded 10 width: {value:010.2f}")

# Percentage formatting
score = 19
total = 22
print(f"\nPercentage: {score/total:.2%}")

# Date formatting
import datetime
today = datetime.datetime.now()
print(f"\nToday is {today:%Y-%m-%d %H:%M:%S}")

# String constants examples
import string
print("\nString constants examples:")
print(f"All digits: {string.digits}")
print(f"All punctuation: {string.punctuation}")

# Template strings example
from string import Template
template = Template("$who likes $what")
print("\nTemplate string example:")
print(template.substitute(who="Alice", what="Python"))