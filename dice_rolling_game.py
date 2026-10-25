import random

while True:
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    question = input("Do you want to roll the dice?: (Yes/No)" ).capitalize()
    if question == "Yes":
        print("🎲 Rolling....")
        print(f"You rolled {die_1} and {die_2}")
        if die_1 == 6 and die_2 == 6:
            print("🎉 Double! Lucky roll!")
    elif question == "No":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choice!")

