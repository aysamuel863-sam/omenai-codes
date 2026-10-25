import random

play_again = "Y"

while play_again.capitalize() == "Y":
    maxn = int(input("Easy (1 - 20)\n"  
                "Medium (1 - 50)\n" 
                "Hard (1 - 100)\n" 
                "So if you want easy, enter 20, medium 50, hard 100.....: "))
  
    n = random.randint(1, maxn)
    print("This is a number guessing game")
    print("My First game actually")
    guess = None
    attempt = 0
    while guess != n:
        try:
            guess = int(input("Attempt: "))
            attempt += 1
            if guess > n:
                print("Too High")
            elif guess < n:
                print("Too Low")
            else:
                print(f"Congratulations, you won in {attempt} attempts")
                break
        except ValueError:
            print("Please enter a number only")
    play_again = input("Play again? (Y/N): ").capitalize()
    
print("Thanks for playing ")

        