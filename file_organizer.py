# file_organizer.py
# Organizes files by extension into subfolders
import os
import shutil

# --- SETTINGS ---
# Folder to organize (use "." for current directory)
SOURCE_DIR = "."

# File type categories
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".rb", ".php"]
}

# --- MAIN ---
def organize_files():
    files_moved = 0

    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                target_dir = os.path.join(SOURCE_DIR, category)
                os.makedirs(target_dir, exist_ok=True)

                new_path = os.path.join(target_dir, filename)

                # Avoid overwriting
                if os.path.exists(new_path):
                    base, ext = os.path.splitext(filename)
                    count = 1
                    while os.path.exists(new_path):
                        new_path = os.path.join(target_dir, f"{base}_{count}{ext}")
                        count += 1

                shutil.move(file_path, new_path)
                print(f"Moved: {filename} → {category}/")
                files_moved += 1
                moved = True
                break

        # Unrecognized extension
        if not moved:
            other_dir = os.path.join(SOURCE_DIR, "Other")
            os.makedirs(other_dir, exist_ok=True)
            new_path = os.path.join(other_dir, filename)
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} → Other/")
            files_moved += 1

    print(f"\n✅ Done! {files_moved} file(s) organized.")

if __name__ == "__main__":
    organize_files()
