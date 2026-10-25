import sqlite3
import hashlib

#Connect to database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

#Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,  X
password_hash TEXT NOT NULL
)
""")
connection.commit()

# Password hashing
def hash_password(password):
    password_bytes = password.encode("utf-8")
    password_hash = hashlib.sha256(password_bytes).hexdigest()
    return password_hash

# Sign up
def sign_up():
    print("\n===== SIGN UP =====")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return
    password_hash = hash_password(password)

    try:
        cursor.execute("""
        INSERT INTO users(username, password_hash)
        VALUES (?, ?)
        """, (username, password_hash), )

        connection.commit()
        print("Account created successfully!")

    except sqlite3.IntegrityError:
        print("That username already exists!")

# Login
def login():
    print("\n===== LOGIN =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    password_hash = hash_password(password)

    cursor.execute("""
    SELECT user_id, username 
    FROM users
    WHERE username = ? AND password_hash = ?
    """, (username, password_hash))

    user = cursor.fetchone()

    if user:
        print(f"\nWelcome back, {user[1]}")
    else:
        print("\nInvalid username or password!")

#View users
def view_users():
    cursor.execute("""
    SELECT user_id, username 
    FROM users
    """)

    users = cursor.fetchall()

    print("\n===== USERS =====")
    if not users:
        print("No users registered.")
    else:
        for user in users:
            print(f"ID: {users[0]} | Username: {user[1]}")

#Main Menu
while True:
    print("\n====================")
    print("\nLOGIN SYSTEM")
    print("\n====================")

    print("\n1.   Sign Up")
    print("2.   Login")
    print("3.   View Users")
    print("4.   Exit")

    choice = input("\nChoose an option: ")
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        view_users()
    elif choice == "4":
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice. Try again.")

#Close Database
connection.close()