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
    return all(x in lettersGuessed for x in [x for x in secretWord])


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    resultp = ""
    lpl = []
    for x in range(len(secretWord)):
        resultp += "_ "
    result = resultp
    for x in lettersGuessed:
        if x in secretWord:
            lpl = find(secretWord, x)
            for li in lpl:
                result = resultp[:li * 2] + x + resultp[li * 2 + 1:]
                resultp = result
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = string.ascii_lowercase
    for x in lettersGuessed:
        if x in abc:
            abcd = abc[:abc.index(x)] + "" + abc[abc.index(x) + 1:]
            abc = abcd
    return abc


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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    lives = 8
    lettersGuessed = []
    while isWordGuessed(secretWord,lettersGuessed) == False and lives > 0:
        print("-------------")
        print("You have {} guesses left.".format(lives))
        print("Available Letters: {}".format(getAvailableLetters(lettersGuessed)))
        guess = input("Please guess a letter: ").lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                lives -= 1
        else: print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
    print("-------------")
    if lives == 0:
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
    if isWordGuessed(secretWord,lettersGuessed) == True:
        print ("Congratulations, you won!")






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
