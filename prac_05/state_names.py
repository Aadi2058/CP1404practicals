"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

# Print all states and names
for code in CODE_TO_NAME:
    print(f"{code} is {CODE_TO_NAME[code]}")

# Input loop with lowercase handling and EAFP approach
state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")