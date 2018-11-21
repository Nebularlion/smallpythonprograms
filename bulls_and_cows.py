import random


def generate_cipher():

    # returns a random sequence of 4 unique digits as list

    cipher = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(4):
        number = random.choice(numbers)
        numbers.remove(number)
        cipher.append(number)
    return cipher
        
def get_bulls_and_cows(cipher, guess):
    """
    takes 2 python lists of length 4 cipher and guess and computes the number
    of bulls and the number of cows as a 2 element tuple
    """
    assert len(cipher) == len(guess) == 4, 'cipher and guess must be lists of length 4'

    cow = 0
    bull = 0
    i = 0
    

    for i in range(len(cipher)):
        for j in range(len(guess)):
            if cipher[i] == guess[j]:
                if i == j:
                    bull = bull + 1
                else:
                    cow = cow + 1
    results = [bull, cow]
    return results

def play_game():
    # this function uses both generate_cipher and get_bulls_and_cows

    cipher = generate_cipher()
    playing = True
    guesses = []
    
    while playing:
        guess = int(input("Enter your guess without spaces:\n"))
        if guess < 1111 or guess > 9999:
            print("Invalid input")
        else:
            guess_array = [int(x) for x in str(guess)]
            if len(guess_array) > len(set(guess_array)):
                print("Invalid input")
            else:
                results = get_bulls_and_cows(cipher, guess_array)
                guesses.append(str(guess) + " bulls: " + str(results[0]) + " cows:" + str(results[1]) )
                for guess_string in guesses:
                    print(guess_string)
                if results[0] == 4:
                    playing = False
                    print("Congratulations!")
        
play_game()  
