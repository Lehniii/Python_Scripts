import os
import shutil
import argparse

def check_fileendings(source_path, destination_path):
    file_categories = {
        ".txt": "txt",
        ".pdf": "pdf",
        ".docx": "documents",
        ".doc": "documents",
        ".xlsx": "documents",
        ".pptx": "documents",
        ".ppt": "documents",
        ".zip": "archives",
        ".rar": "archives",
        ".7z": "archives",
        ".exe": "exe",
        ".mp3": "audio",
        ".wav": "audio",
        ".mp4": "audio",
        ".avi": "audio",
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".tif": "images",
        ".tiff": "images",
        ".bmp": "images",
        ".gif": "images",
        ".py": "code",
        ".js": "code",
        ".css": "code",
        ".html": "code",
        ".htm": "code",
        ".php": "code",
        ".c": "code",
        ".cpp": "code"
    }

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for filename in os.listdir(source_path):
        file_extension = os.path.splitext(filename)[-1].lower()
        destination_folder = file_categories.get(file_extension, "others")

        destination = os.path.join(destination_path, destination_folder)

        if not os.path.exists(destination):
            os.makedirs(destination)

        file_path = os.path.join(source_path, filename)
        shutil.move(file_path, os.path.join(destination, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files by their extensions.")
    parser.add_argument("-sourcepath", type=str, help="Source directory path")
    parser.add_argument("-destinationpath", type=str, help="Destination directory path")

    args = parser.parse_args()

    if args.sourcepath and args.destinationpath:
        check_fileendings(args.sourcepath, args.destinationpath)
    else:
        print("Please provide source and destination paths using -sourcepath and -destinationpath arguments.")





    