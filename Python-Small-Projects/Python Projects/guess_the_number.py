import random
from termcolor import colored

print(colored("Hello and welcome to 'Guess the Number'.", "white"))
print(colored("If you want to leave type quit.", "red"))
print(colored("Enjoy the game! :)", "white"))


def guess():
    random_number = random.randint(1, 10)
    guess = 0

    while guess != random_number:
        guess = (input(colored("Guess a random number between 1 and 10: ", "red")))
        if guess == "quit":
            print("Nice playing with you!")
            exit()

        guess = int(guess)

        if random_number > guess:
            print("Too low!")

        elif random_number < guess:
            print("Too high!")

        elif guess == random_number:
            print(colored("You guessed right!", "yellow"))


guess()