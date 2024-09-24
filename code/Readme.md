Utilitys is a versatile collection of useful functions for file management, 
console output, screen control, and more. This class provides methods for 
writing, reading, copying, and moving files, working with ZIP archives, colored 
console output, UUID generation, email validation, and logging.

---

**Features**:
- File operations
- Screen control
- Colored console output
- ZIP file creation and extraction
- UUID generation
- Email validation
- Logging

**List of Functions**:
- ```writeFile(filename, data)```: Writes data to the specified file. `Returns None`.
- ```appendToFile(filename, data)```: Appends data to the specified file. `Returns None`.
- ```readFile(filename)```: Reads and returns the content of the file. `Returns String (File) / None`.
- ```clearScreen()```: Clears the console screen. `Returns None`.
- ```printColored(text, color="white")```: Prints text in the specified color. `Returns None`.
- ```copyFile(src, dest)```: Copies a file from the source to the destination. `Returns None`.
- ```moveFile(src, dest)```: Moves a file from the source to the destination. `Returns None`.
- ```getFileCreationDate(filename)```: Gets the creation date of the file. `Returns String (Date) / None`.
- ```zipFiles(zip_name, file_list)```: Creates a ZIP file from a list of files. `Returns None`.
- ```unzipFile(zip_name, extract_to)```: Extracts the contents of a ZIP file to the specified directory. `Returns None`.
- ```generateUUID()```: Generates a UUID (Universally Unique Identifier). `Returns String (UUID)`.
- ```isValidEmail(email)```: Checks if the given email address is valid. `Returns Boolean`.
- ```listFilesInDir(dir_path):``` Lists all files in the specified directory. `Returns list`.
- ```log(message)```: Logs a message to the log file. `Returns None`.

---

**Example:**
```python
from utilitys import Utilitys

def main():
    utils = Utilitys()

    # Write to a file
    filename = 'example.txt'
    utils.writeFile(filename, "Hello, this is a sample text.\n")
    print(f"Written to {filename}")

    # Append to the file
    utils.appendToFile(filename, "Appending more text to the file.\n")
    print(f"Appended to {filename}")

    # Read from the file
    content = utils.readFile(filename)
    print(f"Content of {filename}:\n{content}")

    # Clear the screen
    utils.clearScreen()

    # Print colored text
    utils.printColored("This is a red message.", "red")
    utils.printColored("This is a green message.", "green")

    # Copy the file
    copy_filename = 'example_copy.txt'
    utils.copyFile(filename, copy_filename)
    print(f"Copied {filename} to {copy_filename}")

    # Move the file
    moved_filename = 'moved_example.txt'
    utils.moveFile(copy_filename, moved_filename)
    print(f"Moved {copy_filename} to {moved_filename}")

    # Get the creation date of the original file
    creation_date = utils.getFileCreationDate(filename)
    print(f"Creation date of {filename}: {creation_date}")

    # Create a zip file
    zip_name = 'example.zip'
    utils.zipFiles(zip_name, [filename])
    print(f"Created zip file: {zip_name}")

    # Unzip the file
    utils.unzipFile(zip_name, 'unzipped_example')
    print(f"Unzipped {zip_name} to 'unzipped_example' directory")

    # Generate a UUID
    uuid = utils.generateUUID()
    print(f"Generated UUID: {uuid}")

    # Validate an email
    email = "test@example.com"
    is_valid = utils.isValidEmail(email)
    print(f"Is '{email}' a valid email? {is_valid}")

    # List files in the current directory
    files = utils.listFilesInDir('.')
    print(f"Files in current directory: {files}")

    # Log a message
    utils.log("This is a log message for demonstration.")

if __name__ == "__main__":
    main()
```
