import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#word = random.choice(wordslist) 
word="credit card"

#prints the word with * instead of letter until the user guesses the correct letter. 
def print_word(word, letter_guess):
    display_word=""
    for letter in word:
        if letter in letter_guess:
            display_word+=letter
        elif letter == " ":
            display_word+=" "
        else:
            display_word+="*"
    return display_word

#Allows the player to enter a letter to guess. Makes sure the guess is actually a letter and not more then 1 character
def player_guess():
    letter_guess = input("Type a letter you want to guess\n")
    if not letter_guess.isalpha() and not len(letter_guess)==1: 
        letter_guess=input("Not a valid character, try again\n") 
    elif letter_guess in guessed_letters:
        letter_guess=input("Sorry, you've already tried that letter\n")
    return letter_guess

#Checks if the users letter is in the random word
def check_letter_in_word(word,letter_guess):
    if letter_guess in word:
        return True
    else:
        print ("Letter isn't in the word")
        return False

def check_win (computer_word,user_word):
    return computer_word==user_word

def print_hangman(num_guesses):
    if num_guesses==1:
        print(
'''|--------
|       |
|       O
|
|
|
|
|
-------'''
        )

    if num_guesses==2:
        print(
'''|--------
|       |
|       O
|       |
|       
|
|
|
-------'''
        )

    if num_guesses==3:
        print(
            '''|--------
|       |
|       O
|      \\|
|       
|
|
|
-------'''
        )
    if num_guesses==4:
        print(
'''|--------
|       |
|       O
|      \\|/
|       |
|
|
|
-------'''
        )
    if num_guesses==5:
        print(
'''|--------
|       |
|       O
|      \\|/
|       | 
|      /
|
|
-------'''
        )
    if num_guesses==6:
        print(
'''|--------
|       |
|       O
|      \\|/
|       |
|      / \\
|
|
-------'''
        )



if __name__== "__main__":
    guessed_letters=""
    correct_word=""
    print(word)
    print("Welcome to hangman. The computer has chosen a word for you to guess.")
    print(f"The word is {"*" * len(word)} characters long")
    num_turns=0
    #While the game isn't won and the hangman hasn't been 'hung' ie less then 6 turns, run the game
    while not check_win(word,correct_word) and num_turns<6:
        guess=player_guess()
        guessed_letters+=guess
        if not check_letter_in_word(word,guess):
            num_turns+=1
            print_hangman(num_turns)
            
        else:
             print(print_word(word,guessed_letters))
             correct_word=print_word(word,guessed_letters)
             
             
    if check_win(word,correct_word):
        print("Well done, you got the word correct")
            
    else:
        print("You lost :(")
        print(f"The word was {word}")





