"""
CP1404/CP5632 Practical
Hexadecimal colour code lookup program

Estimated time: 20 minutes
Actual time: 25 minutes
"""

COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "blanchedalmond": "#ffebcd",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887"
}

# Input loop with case-independent lookup
colour_name = input("Enter colour name (blank to quit): ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name (blank to quit): ").lower()