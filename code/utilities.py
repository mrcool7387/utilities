import os
import shutil
import zipfile
import logging
import uuid
import re
from datetime import datetime
import colorama

class Utilitys:
    """
    Utilitys is a versatile collection of useful functions for file management, 
    console output, screen control, and more. This class provides methods for 
    writing, reading, copying, and moving files, working with ZIP archives, colored 
    console output, UUID generation, email validation, and logging.
    
    Features:
    - File operations
    - Screen control
    - Colored console output
    - ZIP file creation and extraction
    - UUID generation
    - Email validation
    - Logging

    List of Functions:
    - writeFile(filename, data): Writes data to the specified file. Returns None.
    - appendToFile(filename, data): Appends data to the specified file. Returns None.
    - readFile(filename): Reads and returns the content of the file. Returns the file content as a string or None if the file does not exist.
    - clearScreen(): Clears the console screen. Returns None.
    - printColored(text, color="white"): Prints text in the specified color. Returns None.
    - copyFile(src, dest): Copies a file from the source to the destination. Returns None.
    - moveFile(src, dest): Moves a file from the source to the destination. Returns None.
    - getFileCreationDate(filename): Gets the creation date of the file. Returns the creation date as a string or None if the file does not exist.
    - zipFiles(zip_name, file_list): Creates a ZIP file from a list of files. Returns None.
    - unzipFile(zip_name, extract_to): Extracts the contents of a ZIP file to the specified directory. Returns None.
    - generateUUID(): Generates a UUID (Universally Unique Identifier). Returns the UUID as a string.
    - isValidEmail(email): Checks if the given email address is valid. Returns True if valid, False otherwise.
    - listFilesInDir(dir_path): Lists all files in the specified directory. Returns a list of file names or an empty list if the directory does not exist.
    - log(message): Logs a message to the log file. Returns None.
    """

    def __init__(self):
        """
        Initializes the Utilitys class and sets up logging.
        Also initializes colorama for colored console output.
        """
        logging.basicConfig(filename="app.log", level=logging.INFO)
        colorama.init(autoreset=True)

    def writeFile(self, filename, data):
        """Writes the given data to the specified file."""
        with open(filename, "w") as file:
            file.write(data)
    
    def appendToFile(self, filename, data):
        """Appends the given data to the specified file."""
        with open(filename, "a") as file:
            file.write(data)
    
    def readFile(self, filename):
        """Reads the content of the specified file and returns it."""
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return file.read()
        return None

    def clearScreen(self):
        """Clears the console screen. Works on both Windows and macOS/Linux."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def printColored(self, text, color="white"):
        """Prints the given text in the specified color to the console."""
        colors = {
            "red": colorama.Fore.RED,
            "green": colorama.Fore.GREEN,
            "yellow": colorama.Fore.YELLOW,
            "blue": colorama.Fore.BLUE,
            "magenta": colorama.Fore.MAGENTA,
            "cyan": colorama.Fore.CYAN,
            "white": colorama.Fore.WHITE
        }
        print(colors.get(color.lower(), colorama.Fore.WHITE) + text)

    def copyFile(self, src, dest):
        """Copies a file from a source path to a destination path."""
        shutil.copy(src, dest)

    def moveFile(self, src, dest):
        """Moves a file from a source path to a destination path."""
        shutil.move(src, dest)

    def getFileCreationDate(self, filename):
        """Returns the creation date of the specified file."""
        if os.path.exists(filename):
            creation_time = os.path.getctime(filename)
            return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def zipFiles(self, zip_name, file_list):
        """Creates a ZIP file from a list of files."""
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in file_list:
                zipf.write(file)

    def unzipFile(self, zip_name, extract_to):
        """Extracts a ZIP file to the specified directory."""
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

    def generateUUID(self):
        """Generates a random UUID (Universally Unique Identifier)."""
        return str(uuid.uuid4())

    def isValidEmail(self, email):
        """Validates whether the given email address is valid."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def listFilesInDir(self, dir_path):
        """Lists all files in the specified directory."""
        if os.path.exists(dir_path):
            return os.listdir(dir_path)
        return []

    def log(self, message):
        """Adds a message to the log."""
        logging.info(message)

