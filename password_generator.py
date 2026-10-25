import random
import string

generate_again = "Y"

while generate_again == "Y":
        
    length = int(input("Enter your preferred password length: "))
    low = string.ascii_lowercase
    dig = string.digits + string.ascii_lowercase
    sym = string.punctuation + string.ascii_lowercase 
    upp = string.ascii_uppercase + string.ascii_lowercase
    dig_sym = string.digits + string.punctuation + string.ascii_lowercase 
    dig_upp = string.digits + string.ascii_uppercase + string.ascii_lowercase 
    sym_upp = string.punctuation + string.ascii_uppercase + string.ascii_lowercase 
    dig_sym_upp = string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase 

    password = ""

    digit = input("Include numbers? (Yes/No): ").capitalize()
    symbol = input("Include symbols? (Yes/No): ").capitalize()
    uppercase = input("Include uppercase? (Yes/No): ").capitalize()

    if (digit == "Yes" and
        symbol == "Yes" and
        uppercase == "Yes"):
        for i in range(length):
            password += random.choice(dig_sym_upp)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "Yes" and
        symbol == "Yes" and
        uppercase == "No"):
        for i in range(length):
            password += random.choice(dig_sym)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "Yes" and
        symbol == "No" and
        uppercase == "Yes"):
        for i in range(length):
            password += random.choice(dig_upp)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "Yes" and
        symbol == "No" and
        uppercase == "No"):
        for i in range(length):
            password += random.choice(dig)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "No" and
        symbol == "Yes" and
        uppercase == "Yes"):
        for i in range(length):
            password += random.choice(sym_upp)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "No" and
        symbol == "Yes" and
        uppercase == "No"):
        for i in range(length):
            password += random.choice(sym)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "No" and
        symbol == "No" and
        uppercase == "Yes"):
        for i in range(length):
            password += random.choice(upp)
        print("\nGenerated Password:")
        print(password)
    elif (digit == "No" and
        symbol == "No" and
        uppercase == "No"):
        for i in range(length):
            password += random.choice(low)
        print("\nGenerated Password:")
        print(password)
    else:
        print("Invalid Choice")
    generate_again = input("Generate again? (Y/N): ").capitalize()
    
print("Thank you for using this program")
    