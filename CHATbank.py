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
    with open("aaccounts.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            username, password, balance, account_number = line.split("|")
            accounts[username] = {
            "password": password,
            "balance": float(balance),
            "account_no": account_number
            }
 except FileNotFoundError:
    pass
 return accounts
def save_accounts(accounts):
 with open("accounts.txt", "w") as file:
    for username, details in accounts.items():
        file.write(
        f'{username}|{details["password"]}|'
            f'{details["balance"]}|{details["account_no"]}\n'
    )
class BankAccount:
 def __init__(self, owner, balance, account_number):
    self.owner = owner
    self.balance = balance
    self.account_number = account_number
 def show_balance(self):
    print(f"\n{self.owner}, your balance is N{self.balance:.2f}")
 def deposit(self, amount):
    if amount <= 0:
        print("Amount must be greater than 0.")
        return
    self.balance += amount
    print(f"Deposited N{amount:.2f}")
 def withdraw(self, amount):
    if amount <= 0: 
      print("Amount must be greater than 0.")
      return
    if amount <= self.balance:
        self.balance -= amount
        print(f"Withdrawn N{amount:.2f}")
    else:
        print("Insufficient balance.")
def sign_up(accounts):
 print("\n===== SIGN UP =====")
 username = input("Create a username: ").strip()
 if username == "":
   print("Username cannot be empty.")
   return
 if username in accounts:
   print("Username already exists.")
   return
 password = input("Create a password: ")
 confirm_password = input("Confirm your password: ")
 if password != confirm_password:
   print("Passwords do not match.")
   return
 # Generate the account number ONCE.
 new_account_number = account_no()
 accounts[username] = {
 "password": password,
 "balance": 0.0,
 "account_no": new_account_number
 }
 save_accounts(accounts)
 print(f"Your account number is {new_account_number}")
 print("Sign up successful!")
def login(accounts):
 print("\n===== LOGIN =====")
 username = input("Enter your username: ").strip()
 password = input("Enter your password: ")
 if username not in accounts:
   print("Wrong username.")
   return None
 if accounts[username]["password"] != password:
   print("Wrong password.")
   return None
 print(f"Access granted! Welcome {username}.")
 details = accounts[username]
 return BankAccount(
 username,
 details["balance"],
 details["account_no"]
 )
def account_menu(account, accounts):
 while True:
   print("\n===== ACCOUNT MENU =====")
   print("1. Check balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. Check account number")
   print("5. Logout")
   choice = input("Enter your option: ").strip()
   if choice == "1":
      account.show_balance()
   elif choice == "2":
      try:
         amount = float(input("Enter amount to deposit: "))
         account.deposit(amount)
         accounts[account.owner]["balance"] = account.balance
         save_accounts(accounts)
      except ValueError: print("Please enter a valid number.")
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
      print("Logged out successfully.")
      break
   else:
      print("Invalid choice. Try again.")
def main():
 accounts = load_accounts()
 while True:
   print("\n===== WELCOME TO SAMPAY =====")
   print("1. Login")
   print("2. Sign up")
   print("3. Exit")
   choice = input("Enter your option: ").strip()
   if choice == "1":
      account = login(accounts)
      if account is not None:
         account_menu(account, accounts)
   elif choice == "2":
      sign_up(accounts)
   elif choice == "3":
      print("Thank you for using SamPay. Goodbye!")
      break
   else:
      print("Invalid choice. Try again.")
main()