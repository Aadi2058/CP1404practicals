valid_input = False  # Flag to control the loop

while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Error: Division by zero is not allowed. Please try again.")
            continue  # Skip the rest and ask again

        fraction = numerator / denominator
        print(f"Result: {fraction}")
        valid_input = True  # Exit the loop

    except ValueError:
        print("Error: Please enter valid integers only.")

print("Finished.")