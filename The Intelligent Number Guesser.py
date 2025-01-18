
import random
def number_guesser():
    print("Welcome to The Intelligent Number Guesser!")

    # Get difficulty level from user
    while True:
        try:
            range_choice = int(input(
                "Choose a difficulty level:\n1. Easy (1-50)\n2. Medium (1-100)\nEnter your choice (1/2): "))
            if range_choice == 1:
                number_range = 50
                break
            elif range_choice == 2:
                number_range = 100
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

    # Randomly select a number within the chosen range
    secret_number = random.randint(1, number_range)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {number_range}: "))
            attempts += 1

            if guess < 1 or guess > number_range:
                print(f"Please guess a number within the range (1-{number_range}).")
            elif guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations 👏👏👏👏👏! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guesser()

