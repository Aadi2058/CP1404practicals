"""
CP1404/CP5632 Practical
Wimbledon champions analysis program

Estimated time: 40 minutes
Actual time: 45 minutes
"""

def load_champions_data(filename):
    """Load champions data from CSV file into a list of lists."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header row
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) >= 3:  # Ensure we have enough columns
                champions.append([parts[2].strip(), parts[1].strip()])  # [Champion, Country]
    return champions

def count_champion_wins(champions_data):
    """Count how many times each champion has won using a dictionary."""
    wins = {}
    for champion, _ in champions_data:
        wins[champion] = wins.get(champion, 0) + 1
    return wins

def get_unique_countries(champions_data):
    """Extract unique countries using a set."""
    countries = set()
    for _, country in champions_data:
        countries.add(country)
    return countries

def main():
    """Main function to process and display Wimbledon champions data."""
    filename = "../../../Downloads/wimbledon.csv"
    champions_data = load_champions_data(filename)
    champion_wins = count_champion_wins(champions_data)
    unique_countries = get_unique_countries(champions_data)

    print("Wimbledon Champions: ")
    for champion, win_count in sorted(champion_wins.items()):
        print(f"{champion} {win_count}")
    print(f"These {len(unique_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(unique_countries)))

if __name__ == "__main__":
    main()