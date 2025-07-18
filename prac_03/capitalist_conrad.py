"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100.00, or falls below $1.00, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants with updated values as per requirements
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00  # $1.00
MAX_PRICE = 100.00  # $100.00
INITIAL_PRICE = 10.00  # $10.00
OUTPUT_FILE = "capitalist_conrad_output.txt"

# Initialize variables
price = INITIAL_PRICE
day = 0

# Open the output file for writing
out_file = open(OUTPUT_FILE, 'w')

# Write initial price
print(f"Starting price: ${price:,.2f}", file=out_file)
print(f"Starting price: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    price_change = 0

    # Generate a random integer of 1 or 2
    # If it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # Generate a random floating-point number between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate a random floating-point number between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    # Print to both console and file
    output_line = f"On day {day} price is: ${price:,.2f}"
    print(output_line, file=out_file)
    print(output_line)

# Close the file
out_file.close()

# Final message
print(f"\nSimulation complete after {day} days.")
print(f"Final price: ${price:,.2f}")
print(f"Output saved to {OUTPUT_FILE}")