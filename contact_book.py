# Contact Book
import json

contacts = {}
 
try:
    with open("my_contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}
def save_contact():
    with open("my_contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact():
    contact_name = input("Enter contact name: ").capitalize()
    contact_phone = input("Enter contact phone number: ")
    if len(contact_phone) == 11:
        contacts[contact_name] = contact_phone
        save_contact()
        print("✔ Contact Saved")
    else:
        print("Phone number must be 11 digits")
def search_contact():
    search_name = input("Enter contact name: ").capitalize()
    if search_name in contacts:
        print("Phone Number:", contacts[search_name])
    else:
        print("❌ Contact not found!")
def delete_contact():
    delete_name = input("Enter contact name: ").capitalize()
    if delete_name in contacts:
        print("Phone Number:", contacts[delete_name])
        confirm = input("Are you sure you want to delete this contact? (Yes/No): ").capitalize()
        if confirm == "Yes":
            del contacts[delete_name]
            save_contact()
            print("The contact has been successfully deleted.")
        else:
            print("❌ Contact not found!")
def new_contact():
    new_name = input("Enter contact name: ").capitalize()
    if new_name in contacts:
        print("Current phone number:", contacts[new_name])
        new_phone = input("Enter new phone number: ")
        contacts[new_name] = new_phone
        save_contact()
        print("Contact successfully updated")            
    else:
        print("❌ Contact not found!")
def all_contact(): 
    if contacts:
        print("\nAll Contacts:")
        for key, value in contacts.items():
            print(key, ":", value)
    else:
        print("❌ No contacts saved!")
def exit():
    print("Thank you for using Contact Book!")

while True:
    print("\n======= CONTACT BOOK =======")
    print("1.   Add Contact")
    print("2.   Find Contact")
    print("3.   Delete Contact")
    print("4.   Update Contact")
    print("5.   Show All Contacts")
    print("6.   Exit")

    choice = input("Choose an option: ")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("❌ Invalid Choice. Please choose 1-6.")
        continue        

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        new_contact()
    elif choice == "5":
        all_contact()
    elif choice == "6":
        exit()
        break
        