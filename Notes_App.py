def save_password(password):
    with open("password.txt", "a") as file:
        file.write(f"{password}\n")

def load_password():
    with open("password.txt", "r") as file:
        return file.read()

def password_exists():
    try:
        with open("password.txt", "r"):
            return True
    except FileNotFoundError:
        return False
    
def login():
    while True:
        saved_password = load_password()
        entered_password = input("Enter your password: ")
        if entered_password == saved_password:
            print("Access granted!")
            return True
        else:
            print("Wrong password!")
            choice = input("Do you want to exit? (Y/N): ").capitalize()
            if choice == "N":
                continue
            elif choice == "Y":
                break     
            else:
                print("Invalid choice!")         
            return False
        
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            note = file.read()
            print("\n==== YOUR NOTES ====")
            print(note)
    except FileNotFoundError:
        print("No notes add yet!")

def delete_notes():
    with open("notes.txt", "w") as file:
        file.write("")
    print("All notes deleted!")

def main():
    while True:
        print("\n==== NOTES APP ====" 
            "\n1. Add a Note"
            "\n2. View Notes"
            "\n3. Delete All Notes"
            "\n4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Thank you for using this app, Goodbye!")
            break
        else:
            print("Invalid choice!")

if password_exists():
    print("Password found.")

    if login():
        main()
else:
    while True:
        password = input("Create a password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            print("Password created successfully!")
            save_password(password)
            break
        else:
            print("Passwords do not match. Try again.")

    if login():
        main()