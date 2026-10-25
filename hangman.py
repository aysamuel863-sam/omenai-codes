import random

words = [
    "Python"
    "Java"
    "Javascript"
    "Go"
    "Flask"
    "Ruby"
    "Cup"
    "Ball"
    "Car"
    "Bread"
    "Phone"
    "Laptop"
]
print("This is a Hangman game")
print("One letter at a time")

random_word = random.choice(words)
trial = input("Enter your trial: ")

for i in range(len(random_word)):
    if len(trial) == 1:
        continue
    else:
        break
        print("One letter at a time!")

