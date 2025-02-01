import random

minimum_number = 0
maximum_number = 0
invalid = True
best_score = []
number_of_guesses = random.randint(10, 50)

while invalid:
    try:
        number1 = int(input("Enter the minimum number: "))
        number2 = int(input("Enter the maximum number: "))
        if (number1 > number2) or (number1 < 0) or (number2 < 0):
            raise ValueError
        minimum_number = number1
        maximum_number = number2
        invalid = False
    except ValueError:
        print("Please enter correct values above 0!")

computer_generated_number = random.randint(minimum_number, maximum_number)

while True:
    try:
        guessed_number = int(input(f"Guess the number between {minimum_number} and {maximum_number}: "))
        if guessed_number == computer_generated_number:
            print(f"You guessed it right! The number is: {computer_generated_number}")
            best_score.append(number_of_guesses)
            print(f"Best score: {best_score}")
            break
        else:
            print("You guessed it wrong!")
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("You lost the game!")
                print(f"The correct number is: {computer_generated_number}")
                break
            print(f"You have {number_of_guesses} guesses left.")
            if guessed_number < computer_generated_number:
                print("Try higher number!")
            else:
                print("Try lower number!")
    except ValueError:
        print("Please enter a valid numer!")

