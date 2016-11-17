#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Simulates a match of the Mystery Word, based on the famous
#              Hangman game.
#
# Author:      Andre Costa
#
# Created:     21/10/2014
# Copyright:   (c) 2014
# Licence:     <>
#-------------------------------------------------------------------------------

import funs
# name of the file containing the words
words = "dictionary.txt"
# how many tries the user has
tries = 6
# variable to count the guesses
count = 0
# if found == 1 the word has been found
found = 0
# mid-result to evaluate if the user has reached the final word
result = []
# right guesses are stored here
right = []
# wrong guesses are stored here
misses = []
# current game (number) Example: if we are playing the 3rd game in a row,
# game equals to 3
game = 1
# store the summary of the games played
sgames = {}
# generate a random word using the function generateword
word = funs.generateword(words)
# "populate" the list result with dots
for i in range(0, len(word)):
    result.append('_')

#we are requesting an input until the user runs out of tries or finds the word
while count < tries and found == 0:
    #call the function to show the interface
    funs.interface(result, word, misses)
    #ask for the guess of the user
    guess = raw_input("What is your guess? ")
    #if the guess isn't valid, it will ask again till it's valid
    while not str.isalpha(guess) or funs.checkuse(guess, right, misses) == 1 \
    or len(guess)!=1:
        guess = input("That's not a valid guess! What is your guess? ")
    #if the guess isn't present on the word the variable count increases by 1
    #and the user's guess is stored at the list "misses"
    if funs.evaluate(word, guess, result) == 0:
        misses.append(guess)
        count += 1
    #The opposite happens if the user is right on the guess. The variable count
    #isn't incremented and the guess is stored at the list "right"
    else:
        right.append(guess)
        result = funs.evaluate(word, guess, result)
    #checks if the word has been found after this guess
    found = funs.evalresult(word, result)
    if found == 1:
        #if the user found the word, the data of the game is stored at
        #sgames (with won)
        sgames['g' + str(game)] = 'Game Number ' + str(game) + \
                                  " - You've won this game! " + \
                                  "Tries used - " + str(count) + "/" + \
                                  str(tries) + " | The word was " + word.upper()
        #Ask if the user wants to start a new game
        newgame = raw_input("Congratulations, you've found the word! It's " + \
                                  word.upper() + \
                                  "! Do you want to start a new game? (Y/N)\n")
        while (not str.isalpha(newgame)) or (newgame != 'y' and newgame \
            != 'Y' and newgame != 'n' and newgame != 'N'):
            newgame = raw_input("That's not a valid answer!"
            "Do you want to start a new game? (Y/N)\n")
        #If the user says yes, all variables are reset to the initial state
        #and a new word is generated
        if newgame == 'Y' or newgame == 'y':
            count = 0
            found = 0
            result = []
            right = []
            misses = []
            game += 1
            word = funs.generateword(words)
            for i in range(0, len(word)):
                result.append('_')
    if count == tries:
        #if the user didn't find the word, the data of the game is
        #stored at sgames (with lost)
        sgames['g' + str(game)] = 'Game Number ' + str(game) + \
                                  " - You've lost this game! " + \
                                  "Tries used - " + str(count) + "/" + \
                                  str(tries) + " | The word was " + word.upper()
        newgame = input("You've run out of tries! The word was " + \
                        word.upper() +
                        "! Do you want to start a new game? (Y/N)\n")
        while (not str.isalpha(newgame)) or (newgame != 'y' and newgame != 'Y' \
            and newgame != 'n' and newgame != 'N'):
            newgame = input("That's not a valid answer!"
            "Do you want to start a new game? (Y/N)\n")
        if newgame == 'Y' or newgame == 'y':
            count = 0
            found = 0
            result = []
            right = []
            misses = []
            game += 1
            word = funs.generateword(words)
            for i in range(0, len(word)):
                result.append('_')

if game > 1:
    print("SUMMARY OF YOUR GAMES: ")
    for i in range(1, game + 1):
        print(sgames['g' + str(i)])

elif game == 1:
    print("SUMMARY OF YOUR GAME: ")
    print(sgames['g' + str(game)])

#Sample of the program running
# __  __  __  __
# Misses:
# What is your guess? a
# __  __  __  __
# Misses: a
# What is your guess? e
# __  __  __  __
# Misses: a, e
# What is your guess? i
# __  __  __  __
# Misses: a, e, i
# What is your guess? o
# __  __  __  __
# Misses: a, e, i, o
# What is your guess? u
# __  u  __  __
# Misses: a, e, i, o
# What is your guess? p
# __  u  __  __
# Misses: a, e, i, o, p
# What is your guess? m
# You've run out of tries! The word was RUSH! Do you want to start a new game? (Y/N)
# y
# __  __  __  __  __  __
# Misses:
# What is your guess? a
# __  __  __  __  __  __
# Misses: a
# What is your guess? e
# __  __  e  __  __  __
# Misses: a
# What is your guess? i
# __  __  e  __  __  __
# Misses: a, i
# What is your guess? o
# __  o  e  __  __  __
# Misses: a, i
# What is your guess? t
# __  o  e  t  __  __
# Misses: a, i
# What is your guess? s
# __  o  e  t  __  __
# Misses: a, i, s
# What is your guess? p
# p  o  e  t  __  __
# Misses: a, i, s
# What is your guess? r
# p  o  e  t  r  __
# Misses: a, i, s
# What is your guess? y
# Congratulations, you've found the word! It's POETRY! Do you want to start a new game? (Y/N)
# y
# __  __  __  __  __  __  __
# Misses:
# What is your guess? a
# __  __  __  a  __  __  __
# Misses:
# What is your guess? e
# __  __  e  a  __  e  __
# Misses:
# What is your guess? p
# __  __  e  a  __  e  __
# Misses: p
# What is your guess? s
# __  __  e  a  __  e  __
# Misses: p, s
# What is your guess? t
# t  __  e  a  t  e  __
# Misses: p, s
# What is your guess? r
# t  r  e  a  t  e  __
# Misses: p, s
# What is your guess? n
# t  r  e  a  t  e  __
# Misses: p, s, n
# What is your guess? y
# t  r  e  a  t  e  __
# Misses: p, s, n, y
# What is your guess? l
# t  r  e  a  t  e  __
# Misses: p, s, n, y, l
# What is your guess? u
# You've run out of tries! The word was TREATED! Do you want to start a new game? (Y/N)
# n
# SUMMARY OF YOUR GAMES:
# Game Number 1 - You've lost this game! Tries used - 6/6 | The word was RUSH
# Game Number 2 - You've won this game! Tries used - 3/6 | The word was POETRY
# Game Number 3 - You've lost this game! Tries used - 6/6 | The word was TREATED