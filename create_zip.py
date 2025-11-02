import zipfile
import os

def create_zip():
    # Create a ZIP file
    with zipfile.ZipFile('bisection_assignment.zip', 'w') as zipf:
        # Add all files in the directory except the ZIP file itself and this script
        for file in os.listdir('.'):
            if file != 'bisection_assignment.zip' and file != 'create_zip.py':
                zipf.write(file)
                print(f"Added {file} to ZIP")

    print("ZIP file created successfully: bisection_assignment.zip")

if __name__ == "__main__":
    create_zip()
