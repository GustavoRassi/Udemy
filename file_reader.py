# Developed by: Gustavo Rassi
# Program: File word counter
# Description: Count number of words are in the file

sample_file = "file.txt"

try:
    with open(sample_file, 'r') as file1:
        # Read the content of the file
        content = file1.read()

        # Split the string into substrings and place them in a list of words
        words = content.split()

        # Count how many words are there
        word_count = len(words)

        # Display the file content & number of words to the user
        print(content)
        print(f"Number of words in the file: {word_count}")

except FileNotFoundError: # In case the file doesn't exist
    print("Error: File does not exist.")