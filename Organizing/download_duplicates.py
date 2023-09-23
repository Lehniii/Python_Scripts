import os
import glob

# Define the path to the user's Downloads folder
downloads_folder = os.path.expanduser('~') + '\\Downloads'

# Create a pattern to match files with appended numbers
pattern = os.path.join(downloads_folder, '* (*)*.*')

# Use glob to find files matching the pattern
files_to_delete = glob.glob(pattern)

# Iterate through the files and delete them
for file_path in files_to_delete:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {str(e)}")
