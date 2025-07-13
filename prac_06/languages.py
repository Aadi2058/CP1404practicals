"""
CP1404/CP5632 Practical - Client code for ProgrammingLanguage class
Estimate: 10 minutes
Actual: 7 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Demo test code to show ProgrammingLanguage class usage."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print one language to test __str__()
    print(python)

    # Make list of languages
    languages = [python, ruby, visual_basic]

    # Filter and print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
