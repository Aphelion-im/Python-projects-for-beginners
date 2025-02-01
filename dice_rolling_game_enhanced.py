import random

numbers = []
numberOfRoles = 0

while True:
    choice = input("Do you want to play? y/n: ").lower()
    if choice == "y":
        numberOfRoles += 1
        numbers = []
        number = int(input("How many dice do you want to role? Enter a number: "))
        for _ in range(number):
            numbers.append(random.randint(1, 10))
        print(numbers)
        print(f'Number of roles: {numberOfRoles}')
    elif choice == "n":
        print("Exiting program!")
        break
    else:
        print("Invalid choice!")