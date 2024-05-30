# Improved Guessing Game
#Potential changes- separate min and max input functions so can give feedback immediately
#ask if should be able to quit during range setting

# Marina Music (20496250)
# May 27th, 2024





# Encodes a random number generator that generates a random
# number between 1 and 10 (inclusive) and assigns that number
# to the variable winning_number.

import random                                                    #https://shorturl.at/9uS7J

def getMinMax():
    min_input = input("Please enter a positive, non-zero integer value to set as the guessing range minimum:\n")
    max_input = input("Please enter a positive, non-zero integer value to set as the guessing range maximum:\n")
    return min_input, max_input

def checkMinMax(minimum, maximum):
    if minimum.isnumeric() and maximum.isnumeric():
        if int(maximum) > int(minimum) > 0:
            return 'valid'
        else:
            return 'invalid'
    else:
        return 'invalid'



def generateRandomNumber(minimum, maximum):
    winning_number = random.randrange(minimum, maximum)
    return winning_number

def getGuess(minimum,maximum):
    guess = input(f"Enter an integer number between {minimum} and {maximum} or to give up type \'quit\':\n")
    return guess


def checkGuess(guess, maximum, minimum):
    if guess.isnumeric():
        if maximum >= int(guess) >= minimum:
            return int(guess)
    elif guess.casefold() == 'quit':
        return 'quit'
    else:
        return 'invalid'

def compareNumbers(guess, winning_number):
    if guess == 'quit':
        print(f"\nThe correct answer was {winning_number}. Thanks for letting me win, goodbye!")
        return 'quit'
    else:
        if guess == winning_number:
            print(f"You win! The correct answer was {winning_number}!")
            return 'right'
        elif guess > winning_number:
            print("Wrong! Your guess is too high. Try again.\n")
            return 'wrong'
        else:
            print("Wrong! Your guess is too low. Try again.\n")
            return 'wrong'



def main():
    print("Welcome to the guessing game!\n"
          "You will enter a minimum and maximum value and I will think of a number in that range.\n"
          "Then you will guess the number I'm thinking of! "
          "Let's begin...\n")
    min_max = getMinMax()
    minimum, maximum = min_max              #unpack tuple https://martinxpn.medium.com/what-are-multiple-return-values-actually-in-python-28-100-days-of-python-82821c8de24b#:~:text=In%20Python%2C%20it%20is%20possible,very%20useful%20in%20many%20scenarios.
    check_min_max = checkMinMax(minimum, maximum)
    while check_min_max != 'valid':
        print("Invalid input. Please try again.")
        min_max = getMinMax()
        minimum, maximum = min_max
        check_min_max = checkMinMax(minimum, maximum)
    minimum = int(minimum)
    maximum = int(maximum)
    winning_number = generateRandomNumber(minimum, maximum)
    guess_input = getGuess(minimum, maximum)
    validated_guess = checkGuess(guess_input, maximum, minimum)
    while validated_guess == 'invalid':
        print("Invalid input. Please try again.\n")
        guess_input = getGuess(minimum,maximum)
        validated_guess = checkGuess(guess_input, maximum, minimum)
    right_or_wrong = compareNumbers(validated_guess, winning_number)
    while right_or_wrong == 'wrong' and validated_guess != 'quit':
        guess_input = getGuess(minimum, maximum)
        validated_guess = checkGuess(guess_input, maximum, minimum)
        while validated_guess == 'invalid':
            print("Invalid input. Please try again.\n")
            guess_input = getGuess(minimum, maximum)
            validated_guess = checkGuess(guess_input, maximum, minimum)
        right_or_wrong = compareNumbers(validated_guess, winning_number)





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
        print("win statment and winning_number")
    7. giveUp()- If use types "quit" at any point program should print winning""" # and terminate
main()

