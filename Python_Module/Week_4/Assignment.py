def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            modified_content = content.upper()  # Example modification: convert to uppercase

        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"Successfully wrote the modified content to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while trying to read '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the input filename
input_filename = input("Enter the name of the file to read: ")
output_filename = "modified_" + input_filename

read_and_modify_file(input_filename, output_filename)
