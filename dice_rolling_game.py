import random

while True:
    choice = input("Roll the dice? ").lower()
    if choice == "yes":
        die1 = random.randint(1,10)
        die2 = random.randint(1,10)
        print(f'Die 1: {die1}, Die 2: {die2}')
    elif choice == "No":
        print("Okay! Exiting program!")
        break
    else:
        print("Invalid choice!")
