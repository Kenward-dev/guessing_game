import random

secret_number = random.randint(1, 10)
guess = None
attempts = 0

print("I'm thinking of a number between 1 and 10. Can you guess it?")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    match guess:
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
        case _ if guess > secret_number:
            print("Oops, too high. Try again!")
        case _ if guess == secret_number:
            print(f"Congratulations, you guessed it! It took you {attempts} attempts.")
