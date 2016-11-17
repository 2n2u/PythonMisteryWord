import random


def generateword(words):
    "Returns randomly a word from a text file (the words should be separated by"
    " a whitespace or newline)"
    #Open the file
    fo = open(words)
    #Creation of the list that will contain all the words written in the
    #file "words" assigning for each whitespace or /n an element on the list
    wordlist = fo.read().split()
    #choose randomly an index
    wordchosen = random.randint(0, len(wordlist)-1)
    #access the index on the wordlist and pick a random word
    word = wordlist[wordchosen]
    # Close opened file
    fo.close()
    return word


def interface(result, word, misses):
    "Creates the text interface for one play of the game"
    fresult = ""
    #converts the list result to string (fresult)
    for i in range(0, len(word)):
        fresult += result[i]
    #adds whitespace for each character
    print(" ".join(fresult))
    #adds comma and whitespace for each character
    print("Misses: " + ", ".join(misses))
    return

def evaluate(word, guess, result):
    "Evaluates if the letter guessed is on the word, returns 0 if it isn't"
    "contained otherwise returns the letters used on the mid-result(every right"
    " guesses together)"
    evalu = 0
    for i in range(0, len(word)):
        if word[i] == guess:
            result[i] = guess
            evalu = result
    return evalu

def evalresult(word, result):
    "Evaluates if user reached the word (every letter), if he reached the final"
    " word, returns 1, otherwise returns 0"
    fresult = ""
    for i in range(0, len(word)):
        fresult += result[i]
    if word == fresult:
        return 1
    else:
        return 0

def checkuse(guess, right, misses):
    "Checks if the user's input is equal to a previous guess, returns 1 if"
    " user's input is equal a previous guess, returns 0 otherwise"
    if guess in right:
        return 1
    if guess in misses:
        return 1
    return 0

if __name__ == "__main__":
    interface("programming", "prain", "eds")
