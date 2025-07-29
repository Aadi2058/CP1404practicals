"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
"""

from programming_language import ProgrammingLanguage


def main():
    """Read language data from CSV file and display as objects."""
    languages = load_languages("languages.csv")

    print("All programming languages:")
    for language in languages:
        print(language)

    print("\nDynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


def load_languages(filename):
    """Load programming languages from a CSV file into a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, 'r') as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            typing = parts[1]
            reflection = parts[2] == "Yes"
            year = int(parts[3])
            language = ProgrammingLanguage(name, typing, reflection, year)
            languages.append(language)
    return languages


if __name__ == '__main__':
    main()
