
import random

def main():

    print("Welcome to the guessing game!")

    while True:

        print("Starting a new game...")
        Game()
        if not ask_to_play_again():
            print("Thank you for playing!")
            break

def Game():
    randomNumber = random.randrange(1,20)
    guess_i = 0

    while True:
        userInput = input("Guess a number between 1-20 (n = new game, x = exit game, s = cheat):").lower()
        
        if userInput == "x":
            print("Exiting game")
            exit()
        elif userInput == "s":
            print(f"The hidden number is {randomNumber}")
            guess_i += 1
            continue
        elif userInput == "n":
            break

        try:
            userGuess = int(userInput)
            guess_i += 1

            if userGuess < randomNumber:
                print("The guess is too small.")
            elif userGuess > randomNumber:
                print("The guess is too big.")
            elif userGuess == randomNumber:
                print(f"You win after guessing {guess_i} times!")
                break
        except ValueError:
            print("Invalid input. Provide a number between 1-20 or select next action (x, n, s).")

def ask_to_play_again():

    while True:
        replay = input("Do you want to play another game? (y/n): ").lower()
        if replay in ["y", "n"]:
            return replay == "y"
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

