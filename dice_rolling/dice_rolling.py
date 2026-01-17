import random

while True:
    choice  = input("Roll the Dice (Y/N): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"{dice1} vs {dice2}")
    elif choice == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid input")