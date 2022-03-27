# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += "_ "
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    okletters= list(string.ascii_lowercase)
    for letter in lettersGuessed:
        okletters.remove(letter)

    okstr = ""
    for char in okletters:
        okstr += char

    return okstr

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    availableletters = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secretWord)} letters long.")
    print("Available letters: ", availableletters)
    guesses = 10
    lettersGuessed = []
    str = getGuessedWord(secretWord,lettersGuessed)

    while not isWordGuessed(secretWord, lettersGuessed) and guesses != 0:
        print("------------")
        print(f"You have {guesses} guesses left. ")
        print("Available letters: ", availableletters)
        guess = input("Please guess a letter: ")

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", str)
        elif guess in secretWord:
            lettersGuessed.append(guess)
            str = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess: ", str)
            availableletters = getAvailableLetters(lettersGuessed)
        else:
            lettersGuessed.append(guess)
            str = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! That letter is not in my words: ", str)
            guesses -= 1

    if isWordGuessed(secretWord, lettersGuessed):
        print("You Won!")
    else:
        print("Failure, you are..")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
