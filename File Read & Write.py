def process_file(input_filename, output_filename):
    try:
        # Try to open the input file for reading
        with open(input_filename, "r") as file:
            contents = file.read()
        
        # Modify the contents (example: convert all to uppercase)
        modified_contents = contents.upper()
        
        # Write the modified contents to the output file
        with open(output_filename, "w") as file:
            file.write(modified_contents)
        
        print(f"File '{output_filename}' created successfully with modified content.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input filename
    input_filename = input("Enter the input filename: ").strip()
    # Define the output filename (you can customize this)
    output_filename = "modified_" + input_filename
    
    # Process the file
    process_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
