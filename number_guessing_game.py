import random

computer_generated_number = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input("Guess the number between 1 and 100: "))
        if guessed_number == computer_generated_number:
            print(f"You guessed it right! The number is: {computer_generated_number}")
            break
        else:
            print("You guessed it wrong!")
            if guessed_number < computer_generated_number:
                print("Try higher number!")
            else:
                print("Try lower number!")
    except ValueError:
        print("Please enter a valid numer!")
