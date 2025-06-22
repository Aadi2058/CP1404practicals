"""
CP1404/CP5632 Practical
Word occurrence counter program

Estimated time: 30 minutes
Actual time: 35 minutes
"""

# Get input from user
text = input("Text: ")

# Create dictionary to store word counts
word_counts = {}
for word in text.split():
    word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

# Find the longest word length for formatting
max_length = max(len(word) for word in word_counts.keys())

# Sort and print word counts with aligned formatting
for word in sorted(word_counts.keys()):
    print(f"{word:{max_length}} : {word_counts[word]}")