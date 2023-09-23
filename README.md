# Python_Scripts
Just some scripts feel free to use and change

## Organizing:
### sortfiles.py
This script organizes files from a source directory into different destination folders based on their file extensions. It creates the necessary destination folders if they don't exist and ensures that files are moved to their corresponding categorized folders, making it easier to manage and access files of different types.

**Usage:**
python sortfiles.py -sourcepath "sourcepath" -destinationpath "destinationpath"


### download_duplicates.py
This script automatically finds and removes duplicate files with appended numbers in the filenames from your Windows Downloads folder, helping you keep your Downloads folder organized and clutter-free. Use it with caution and consider backing up important files before running the script.

**Usage:**
python download_duplicates.py





## Tools
### password.py
This script generates random passwords of user-defined length and optionally includes special characters. It copies the generated password to the clipboard.

**Usage:**

pip install pyperclip

python password.py

Type your password length then type yes/no if you want special characters


### ToDoPy.py
This script is a simple ToDo List managing app with a tkinter UI. It saves the ToDo's on close of the app in a textfile called todo_list.txt. A Icon.png in the Basefolder is required. The provided icon is from: <a href="https://www.flaticon.com/de/kostenlose-icons/liste" title="liste Icons">List Icon created by Kiranshastry - Flaticon</a>

**Usage:**
python ToDoPy.py
Then use the simple UI
