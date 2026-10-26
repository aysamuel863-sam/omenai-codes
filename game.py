import random

maxn = 10
n = random.randint(1, maxn)
print("This is a number guessing game")
print("My first game actually")
print("Guess a number from 1 to 10")
guess = None
attempts= 0
while guess != n:
    guess = int(input("Attempt:"))
    attempts = attempts+ 1
    if guess > n:
        print("Too high")
    elif guess < n:
        print("Too low")
print("Congratulations, you won in " + str(attempts) + " attempts")