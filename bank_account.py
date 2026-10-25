import random
import string

random_no = string.digits
length = 10
account_no = ""
for i in range(length):
    account_no += random.choice(random_no)

def save_password(password): 
    with open("bank.txt", "a") as file:
        file.write(f"{password}\n")

def load_password():
    with open("bank.txt", "r") as file:
        return file.read()
 
def save_username(username):
    with open("bankk.txt", "a") as file:
        file.write(f"{username}\n")

def load_username():
    with open("bankk.txt", "r") as file:
        return file.read()

def sign_up():
        username = input("Enter a Username: ").capitalize()
        para = "\n"
        save_username(username)
        while True:
            password = input("Create a password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                print("Sign Up Successful!")
                save_password(password)
                print(f"Your account number is {account_no}")
                break
            else:
                print("Passwords do not match. Try again.")

def login():
    saved_password = load_password()
    saved_username = load_username()
    entered_username = input("Enter your username: ").capitalize()
    entered_password = input("Enter your password: ")
    if entered_password == save_password(entered_password) and entered_username == save_username(entered_username):
        print("Access granted!")
        return True
    elif entered_password != saved_password and entered_username == saved_username:
        print("Wrong password!")
    elif entered_password == saved_password and entered_username != saved_username:
        print("Wrong username!")
    else:
        print("Wrong password and wrong username!")
        return False
    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(self.owner, "has", self.balance)
        with open("b.txt", "a") as file:
            file.write(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            ("Deposited", amount)
            with open("b.txt", "a") as file:
                file.write(self.balance)
        else:
            print("Amount must be greater than 0")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn", amount)
            with open("b.txt", "a") as file:
                file.write(self.balance)
        else:
            print("Insufficient balance")
        
def all():
        if login():
            user = BankAccount(save_username(), 0)
            while True:
                print("1.   Check balance")
                print("2.   Deposit")
                print("3.   Withdraw")
                print("4.   Check account number")
                print("5.   Exit")

                choice2 = input("Enter your option: ")
                if choice2 == "1":
                    user.show_balance()
                elif choice2 == "2":
                    try:
                        amount = int(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    except ValueError:
                        print("Please enter a number only!")
                elif choice2 == "3":
                    try:
                        amount = int(input("Enter amount to withdraw: "))       
                        user.withdraw(amount)
                    except ValueError:
                        print("Please enter a number only!")
                elif choice2 == "4":
                    print(account_no)
                elif choice2 == "5":
                    break
                else:
                    print("Invalid choice! Try again.")

def main():
    print("==== Welcome to SamPay! ====")
    print("1.   Login to your account")
    print("2.   New to SamPay? Sign Up")

    choice1 = input("Enter your option: ")
    if choice1 == "1":
        all()
    elif choice1 == "2":
        sign_up()
        all()

main()

