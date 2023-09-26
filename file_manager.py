# Program: Reads and writes text to a text file
# Developer: Gustavo Rassi
# Date; 9/25/2023

sample_file2 = "file2.txt"

# Store some text to pass it to the .txt file
text_info = "Hello, I can write and read this file!"

try:
    # Make the file readable and writable with '+'
    with open(sample_file2, '+') as file2:
        # Write a text in the file
        file2.write(text_info)

        # Print if file is readable
        if file2.readable() == True:
            content = file2.read()
            print(content)
        else:
            # File is not readable
            print("Error: File is not readable.")

# Exception has occurred
except FileNotFoundError:
    print(f"Error: File {sample_file2} does not exist.")