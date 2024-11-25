import random

def guess_the_number():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    attempts = 0

    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congrats! You guessed it in {attempts} attempts.")
            break

guess_the_number()