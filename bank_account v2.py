import random
import string
def account_no():
    digits = string.digits
    length = 10
    account_number = ""
    for _ in range(length):
        account_number += random.choice(digits)
    return account_number

def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                account_number, username, password, balance = line.split("|")

                account_number = account_number.strip()
                username = username.strip()
                password = password.strip()
                balance = balance.strip()
      

                accounts["account_number"] = {
                    "username": username, "password": password, "balance": float(balance)
                }   
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for account_number, details in accounts.items():
            file.write(f"{"account_number"} | {details["username"]} | {details["password"]} | {details["balance"]}\n")

class BankAccount:
    def __init__(self, balance, account_number):
        #self.owner = owner
        self.balance = balance
        self.account_number = account_number

    def show_balance(self):
        print(f"\nYour balance is N{self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        self.balance += amount
        (f"Deposited, N{amount:.2f}")
        
    def withdraw(self, amount): 
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn N{amount:.2f}")
            
        else:
            print("Insufficient balance")

def transfer(accounts):
    accounts = load_accounts()
    #details = accounts[username]
    try:
        recipient_acc = int(input("Enter recipient account number: "))
        if recipient_acc not in accounts:
            print("This account number does not exists!")
            return
        print(accounts["recipient_acc"]["username"])
        go_on = input("Continue: (Y/N)").upper()
        if go_on == "Y":
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Amount cannot be lesser than or equal to zero!")
            if accounts["account_number"]["balance"] < amount:
                print("Insufficient funds!")
            amount -= accounts["account_number"]["balance"]
            amount += accounts["recipient_acc"]["balance"]
    except ValueError:
        print("Enter a number!")
"""
    try:
            for username, details in accounts.items():
            recipient_account = int(input("Enter amount number: "))
            #recipient_balance = accounts[recipient_username]["balance"]
            #recipient_username = accounts[][recipient_account]
            #recipient_username = accounts[0]
            with open("accounts.txt", "r") as file:
                for line in file:
                    for recipient_account in accounts:
                        recipient_username = accounts[username]
                        recipient_balance = accounts[username]["balance"]
                        recipient_password = accounts[username]["balance"]
            #if recipient_account in accounts[recipient_username]:
            print(recipient_username, ":", recipient_account)
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be greater than 0")
                password = input("Enter your password: ")
                if password == accounts[username]["password"]:
                    recipient_balance += amount
                    accounts[username]["balance"] -= amount
                    save_accounts(accounts)
            except ValueError:
                print("Enter a valid number!")
    except ValueError:
        print("Enter a valid number!")
"""
                
def sign_up(accounts):
    print("\n===== SIGN UP =====")
    account_number = account_no()
    username = input("Create a username: ").strip()
    if username == "":
        print("Username cannot be empty.")
    if username in accounts[account_number]:
        print("Username already exists.")
        return
    password = input("Create a password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match")
        return

  

    accounts[account_number] = {
        "username": username,
        "password": password, 
        "balance": 0.0
    }

    save_accounts(accounts)

    print(f"Your account number is {account_number}")
    print("Sign up successful!")

def login(accounts):
    print("\n===== LOGIN =====")
    account_number = input("Enter your account number: ").strip()
    #username = input("Enter your username: ").strip()
    password = input("Enter your password: ")
    if account_number not in accounts:
        print("Account number does not exist!")
    """if username not in accounts[account_number]:
        print("Wrong username.")
        return None"""
    if accounts[account_number]["password"] != password:
        print("Wrong password.")
        return None

    #print(f"Access granted! Welcome {username}.")

    details = accounts["account_number"]

    return BankAccount(details["balance"], account_number)

def account_menu(account, accounts):
    while True:
        print("\n===== ACCOUNT MENU =====")
        print("1.   Check balance")
        print("2.   Deposit")
        print("3.   Withdraw")
        print("4.   Check account number")
        print("5.   Transfer")
        print("6.   Logout")

        choice = input("Enter your option: ")

        if choice == "1":
            account.show_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                accounts[account.owner]["balance"] = account.balance
                save_accounts(accounts)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
                accounts[account.owner]["balance"] = account.balance
                save_accounts(accounts)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print(f"Your account number is {account.account_number}")
        elif choice == "5":
            transfer(accounts)
        elif choice == "6":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    accounts = load_accounts()

    while True:
        print("\n===== WELCOME TO SAMPAY =====")
        print("1.   Login")
        print("2.   Sign up")
        print("3.   Exit")

        choice = input("Enter your option: ").strip()
        if choice == "1":
            account = login(accounts)
            if account is not None:
                account_menu(account, accounts)
        elif choice == "2":
            sign_up(accounts)
        elif choice == "3":
            print("Thank you for using SamPay, Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
#new_account_number = account_no
#print(new_account_number)ut