import os
import shutil
import logging
from pathlib import Path

# Predefined common folder paths
COMMON_FOLDERS = {
    "1": ("Desktop", r"C:\Users\pulig\OneDrive\Desktop"),
    "2": ("Downloads", os.path.join(Path.home(), "Downloads")),
    "3": ("Documents", r"C:\Users\pulig\OneDrive\Documents"),
    "4": ("Pictures", r"C:\Users\pulig\OneDrive\Pictures"),
    "5": ("Videos", os.path.join(Path.home(), "Videos")),
    "6": ("Choose custom path", None)
}

# Setup logging
logging.basicConfig(filename='organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# File categories
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.csv', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Executables': ['.exe', '.apk', '.bat'],
    'Others': []
}

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                category = get_category(ext)

                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                new_file_path = os.path.join(category_folder, filename)
                shutil.move(file_path, new_file_path)
                logging.info(f"Moved: {filename} -> {category}/")
        print(f"\n✅ Files organized successfully in: {folder_path}")
    except Exception as e:
        logging.error(f"Error: {e}")
        print("❌ Something went wrong. Check organizer.log")

# --- Start ---
print("📁 Choose a folder to organize:")
for key, (name, _) in COMMON_FOLDERS.items():
    print(f"{key}. {name}")

choice = input("Enter your choice (1–6): ")

if choice in COMMON_FOLDERS:
    folder_name, folder_path = COMMON_FOLDERS[choice]
    
    if choice == "6":
        folder_path = input("📂 Enter full path of the folder: ")

    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist.")
    else:
        organize_folder(folder_path)
else:
    print("❌ Invalid choice.")