import string

def check_password(password):
    special = string.punctuation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits

    length = len(password) >= 12
    upper_con = any(char in upper for char in password)
    lower_con = any(char in lower for char in password)
    digit_con = any(char in digit for char in password)
    special_con = any(char in special for char in password)

    print("\nPassword analysis:")
    if not length:
        print("Password must be at least 12 characters.")
    else:
        print("Length requirement passed.")
    if not upper_con:
        print("Password needs an uppercase letter.")
    else:
        print("Contains an uppercase letter.")
    if not lower_con:
        print("Password needs a lowercase letter.")
    else:
        print("Contains an lowercase letter.")
    if not digit_con:
        print("Password needs a number.")
    else:
        print("Contains a number.")
    if not special_con:
        print("Password needs a special character.")
    else:
        print("Contains special character.")

    if length and upper_con and lower_con and digit_con and special_con:
        print("\nThis is a strong password")
    else:
        print("\nThis is a weak password")

    score = 0
    if length:
        score += 1
    if upper_con:
        score += 1
    if lower_con:
        score += 1
    if digit_con:
        score += 1
    if special_con:
        score += 1

    print(f"\nPassword score: {score}/5")
    if score == 5:
        print("STRENGTH: VERY STRONG")
    elif score == 4:
        print("STRENGTH: STRONG")  
    elif score == 3:
        print("STRENGTH: MODERATE")
    elif score >= 1:
        print("STRENGTH: WEAK")
    else:
        print("STRENGTH: VERY WEAK")

    return score

check_again = "Y"

while check_again == "Y":
    password = input("Enter your password: ")
    score = check_password(password)

    check_again = input("Check again? (Y/N): ").capitalize()

print("Thank you for using this program")
