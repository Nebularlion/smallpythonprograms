OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'

def initialize(word_list):

    i = 0
    while i < len(word_list) and start_new_game(word_list[i], 10):
        i += 1
        

def obfuscate(word, letters_guessed):

    game_word = []
    
    for letter in range(len(word)):
        game_word.append("_")

    for i in range(len(letters_guessed)):
        for j in range(len(word)):
            if letters_guessed[i].lower() == word[j].lower():
                game_word[j] = letters_guessed[i]

    
    return game_word

def start_new_game(word, max_tries):

    listed_word = None
    players_guess = None
    guessed_words = []
    letters_guessed = []
    

    game_word = obfuscate(word, letters_guessed)

    while max_tries !=0 and "_" in game_word:
        print(REMAINING_TRIES + " " + str(max_tries))
        listed_word = "".join(guessed_words)
        print(listed_word)

        
        players_guess = input("Please select a letter between A-Z" + " ")
        
            
        
        if players_guess.isalpha()==False:
            print(INVALID_INPUT)
            continue
        elif len(players_guess) > 1:
            print (INVALID_INPUT)
            continue
        elif players_guess in letters_guessed:
            print (INVALID_INPUT)
            continue
        else:
            pass

            
            players_guess = players_guess.lower()
            letters_guessed.append(players_guess)

            if players_guess not in word:
                max_tries = max_tries - 1
                  
            game_word = obfuscate(word, letters_guessed)
            print("".join(game_word))
            
            if "_" not in game_word:
                print(GAME_WON_PHRASE.format(word))
        
    

    response = input(OFFER_NEXT_GAME).lower()
    if response not in ("y", "yes") or ("n", "no"):
        print (INVALID_INPUT)
    if response is ("y", "yes"):
        return True
    else:
        return False


initialize(['ObiWanKenobi', 'Alladin', 'Flower', 'Project', 'Python', 'Reindeer', 'Navigation', 'Library', 'Cockatiel'])

