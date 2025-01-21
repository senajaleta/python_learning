import random
def intelligent_guess():

    guess = 0
    while True:
        level =int(input("choice the level:\n 1 for (1-50)\n 2 for (1-100)\n"))
        if level == 1:
            number_range = 50
            break
        elif level == 2:
            number_range = 100
            break
        else:
         print("invalid level..select 1 0r 2")
         break
    secret_number = random.randint(1, number_range)

    attempts = 0
    while True:
        guess = int(input(f"guess what is the number🤦‍♂️ (1-{number_range}):"))
        attempts += 1

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print(f"you got it 👏👏👏👏👏{secret_number} in {attempts} attempts")
            break
intelligent_guess()
