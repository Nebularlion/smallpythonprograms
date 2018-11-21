import random
import math

play_again = True

while play_again == True:
    min, max = (input("Please enter two value for range:\n").split(','))
    min = int(min)
    max = int(max)
    print ("I have picked a number between " + str(min) + " and " + str(max) + ", whats your guess?")

    number = random.randint(min, max)
    guessed = False
    tries = math.ceil(math.log2(max-min))
    while guessed == False and tries > 0:
        guess = int(input("You have " + str(tries) + " tries left.\n"))
        
        if guess == number:
            print ("You win!")
            guessed = True
        elif guess > number:
            print ("l")
            tries = tries - 1
        elif guess < number:
            print("h")
            tries = tries - 1

    new_game = input("Would you like to play again? y/n\n")
    if new_game == "y":
        play_again = True
    else:
        play_again = False
    
