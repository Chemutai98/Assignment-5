# file_handling_assignment.py

def create_file():
    """Create a new file and write some initial content."""
    try:
        # Open the file in write mode, creating it if it doesn't exist
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line with a number: 123\n")
            file.write("Finally, the third line with more text.\n")
        print("File created and initial content written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating file: {e}")
    finally:
        print("File creation attempt completed.")

def read_file():
    """Read and display the contents of the file."""
    try:
        # Open the file in read mode
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading file: {e}")
    finally:
        print("File reading attempt completed.")

def append_to_file():
    """Append additional lines to the file."""
    try:
        # Open the file in append mode
        with open('my_file.txt', 'a') as file:
            file.write("Adding a new line to the file.\n")
            file.write("Another appended line.\n")
            file.write("And one more line at the end.\n")
        print("Content appended to file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to file: {e}")
    finally:
        print("File appending attempt completed.")

def main():
    """Main function to execute file handling tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show appended content

if __name__ == "__main__":
    main()
