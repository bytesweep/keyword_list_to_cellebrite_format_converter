import sys
import os

def main():
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Please drag and drop a single text file onto the script.")
        return

    # Get the file path from the command line arguments
    input_file_path = sys.argv[1]

    # Check if the file exists and is a file
    if not os.path.isfile(input_file_path):
        print(f"File '{input_file_path}' does not exist or is not a valid file.")
        return

    # Read all lines from the file
    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()

    # Join the lines into a single string with each word separated by a comma and a space
    single_line = ", ".join(lines)

    # Get the directory, filename, and extension parts
    directory = os.path.dirname(input_file_path)
    filename, extension = os.path.splitext(os.path.basename(input_file_path))

    # Create the new filename with the "-CELLEBRITE" suffix
    new_filename = f"{filename}-CELLEBRITE{extension}"
    new_file_path = os.path.join(directory, new_filename)

    # Write the single line string to the new file
    with open(new_file_path, 'w') as file:
        file.write(single_line)

    print(f"File saved as {new_file_path}")

if __name__ == "__main__":
    main()
