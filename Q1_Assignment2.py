# Improved Guessing Game
# Potential changes - separate min and max input functions so can give feedback immediately
# ask if should be able to quit during range setting

# Marina Music (20496250)
# May 27th, 2024


# Encodes a random number generator that generates a random
# number between 1 and 10 (inclusive) and assigns that number
# to the variable winning_number.

import random  # https://shorturl.at/9uS7J
from typing import Union


def get_min_max() -> (str, str):
    min_input = input("Please enter a positive, non-zero integer value to set as the guessing range minimum:\n")
    max_input = input("Please enter a positive, non-zero integer value to set as the guessing range maximum:\n")
    return min_input, max_input


def validate_min_max(minimum: str, maximum: str) -> bool:
    return minimum.isnumeric() and maximum.isnumeric() and int(maximum) > int(minimum) > 0


def generate_random_number(minimum, maximum):
    return random.randrange(minimum, maximum)


def get_guess(minimum: int, maximum: int) -> str:
    return input(f"Enter an integer number between {minimum} and {maximum} or to give up type \'quit\':\n")


def check_guess(guess: str, maximum: int, minimum: int) -> Union[str, int]:
    if guess.isnumeric() and maximum >= int(guess) >= minimum:
        return int(guess)
    elif guess.casefold() == 'quit':
        return 'quit'
    else:
        return 'invalid'


def is_valid_answer(guess: str, winning_number: int) -> bool:
    if guess == 'quit':
        print(f"\nThe correct answer was {winning_number}. Thanks for letting me win, goodbye!")
        return True
    else:
        if guess == winning_number:
            print(f"You win! The correct answer was {winning_number}!")
            return True
        elif int(guess) > winning_number:
            print("Wrong! Your guess is too high. Try again.\n")
            return False
        else:
            print("Wrong! Your guess is too low. Try again.\n")
            return False


def main():
    print("Welcome to the guessing game!\n"
          "You will enter a minimum and maximum value and I will think of a number in that range.\n"
          "Then you will guess the number I'm thinking of! "
          "Let's begin...\n")

    while True:
        min_input, max_input = get_min_max()
        is_valid = validate_min_max(min_input, max_input)
        if is_valid:
            break
        else:
            print("Invalid input. Please try again.")

    minimum = int(min_input)
    maximum = int(max_input)

    winning_number = generate_random_number(minimum, maximum)

    while True:
        while True:
            guess_input = get_guess(minimum, maximum)
            validated_guess = check_guess(guess_input, maximum, minimum)
            if validated_guess != 'invalid':
                break
            else:
                print("Invalid input. Please try again.\n")

        game_over = is_valid_answer(validated_guess, winning_number)

        if game_over:
            break

    """1. Prompt user for min and max value
    - ask for min input
    - ask for max input
    2. Ensure max > min > 0
    - if true generate number
    - if false let know and re-prompt

    3. Generate random number in range

    4. def getGuess to get input from user
    5. Check if input .isnumeric() and is in range(min,max)
        Else
        - print("Invalid input") and getGuess() again

    6.
    -  while guess != winning_number:   allow user to guess until correct value
        - if guess > winning_number:    tell user if higher or lower
            - print("Too low")
            - guess = getGuess()
        - elif guess < winning_number:
            - print("Too high")
            - guess = getGuess()
    6. Win: If guess == winning_number:
        print("win statement and winning_number")
    7. giveUp()- If use types "quit" at any point program should print winning"""  # and terminate


main()
