
FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert student count to integer
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject_info in data:
        print(f"{subject_info[0]} is taught by {subject_info[1]:<12} and has {subject_info[2]:>3} students")


main()