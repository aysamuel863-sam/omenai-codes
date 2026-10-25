import hashlib
import json

def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as file:
        data = file.read()
    sha256.update(data)
    return sha256.hexdigest()

def load_baselines():
    try:
        with open("baselines.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("baselines.json is corrupted or invalid.")
        print("Starting with an empty baseline list.")
        return

def save_hash(filename, file_hash, baselines):
    try:
        baselines[filename] = file_hash
        with open("baselines.json", "w") as file:
            json.dump(baselines, file, indent=4)
    except FileNotFoundError:
        print("File not found!")
def verify_file(filename, baselines):
    try:
        current_hash = calculate_hash(filename)
        if filename not in baselines:
            print("No baseline exists for this file.")
            print("Create a baseline first.")
            return
        original_hash = baselines[filename]
        if current_hash == original_hash:
            print("File is unchanged. Integrity verified.")
        else:
            print("WARNING: File has been modified!")
    except FileNotFoundError:
        print("File not found.")

def list_baselines(baselines):
    print("\n===== MONITORED FILES =====")
    if not baselines:
        print("No files are currently been monitored.")
        return
    for filename in baselines:
        print(f"- {filename}")

def remove_baselines(filename, baselines):
    if filename not in baselines:
        print("This file is not being monitored.")
        return
    del baselines[filename]
    with open("baselines.json", "w") as file:
        json.dump(baselines, file, indent=4)
    print("File removed from monitoring")

def main():
    baselines = load_baselines()
    while True:
        print("\n===== FILE INTEGRITY CHECKER =====")
        print("1.   Create baseline hash")
        print("2.   Verify file")
        print("3.   List monitored files")
        print("4.   Remove monitored files")
        print("5.   Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            filename = input("Enter the file name: ")
            try:
                file_hash = calculate_hash(filename)
                save_hash(filename, file_hash, baselines)
                print("\nBaseline hash saved.")
                print(f"SHA-256: {file_hash}")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "2":
            filename = input("Enter the file name: ")
            verify_file(filename, baselines)
        elif choice == "3":
            list_baselines(baselines)
        elif choice == "4":
            filename = input("Enter the file name to remove: ")
            remove_baselines(filename, baselines)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()