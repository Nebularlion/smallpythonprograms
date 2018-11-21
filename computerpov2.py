import random
import math
play_again = True

while play_again == True:
    min = int(input("What your minimum number?\n"))
    max = int(input("What your maximum number?\n"))

    tries = math.ceil(math.log2(max-min))
    guessed = False
    while guessed == False and tries > 0:
        guess = math.ceil((min + max) / 2)
        print( str(guess) + " Is this your number? h/l/y")
        answer = input()
        if answer == "h":
            min = guess
            tries = tries - 1
        elif answer == "l":
            max = guess
            tries = tries - 1
        elif answer == "y":
            print("Woah, that was tricky!")
            guessed = True
        else:
            print("That is invalid input")

    new_game = input("Would you like to play again? y/n\n")

    if new_game == "y":
        play_again = True
    else:
        play_again = False
