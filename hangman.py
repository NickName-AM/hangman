#!/usr/bin/env python3

# A Game of hangman

import random
import os
from time import sleep

hangman = [
'''
  O
''',
'''
  O
  |
''',
'''
  O
 /|
''',
r'''
  O
 /|\
''',
r'''
  O
 /|\
  |
''',
r'''
  O
 /|\
  |
 /
''',
r'''
  O
 /|\
  |
 / \
'''
]

# Clear the screen
def clear():
  os.system('clear')

# hangman structure ,'_'s and already typed letters
def createStructure():
  clear()
  print(hangman[man])
  print('\n')
  print(' '.join(hiddenLetters))
  print(' '.join(alreadyTyped))
  print('\n')

# Fill '_' with correctly guessed letters
def wordFill(guess):
  i = 0
  for j in word:
    if guess == j.lower():
      hiddenLetters[i] = j
    i += 1

# Fill '_' with spaces
def fillSpace():
  i = 0
  for _ in word:
    if word[i] == ' ':
      hiddenLetters[i] = ' '
    i += 1

# Get the letter from user
def getGuess():
  createStructure()

  guess = input('> ').lower()
  while guess in alreadyTyped or len(guess) != 1:
    createStructure()
    print('Already typed.')
    guess = input('> ')
  alreadyTyped.append(guess)
  return guess

# Check if you won or lost
def check():
  clear()
  if chance == 7 and ''.join(hiddenLetters) != word:
    print('You Lose.')
    print('The correct word(s) : ' + word)
    exit()
  elif ''.join(hiddenLetters) == word:
    print('You win.')

    print('Word(s): ' + word)
    exit()

# Choose a random word from given file
def chooseRandomWord():
  with open(FILENAME) as f:
    wordList = f.readlines()
  chosenWord = random.choice(wordList)[:-1]
  return chosenWord

# Main
def play():
  global man
  global chance
  while True:
    guess = getGuess()
    if guess in word.lower():
      wordFill(guess)
    else:
      man-=1
      chance+=1
  
    check()


# Filename with words
FILENAME='words.txt'

# Choose random word(s) from the file
word = chooseRandomWord()

# The _'s
hiddenLetters = ['_'] * len(word)

# Fill '_' with ' ' if there are spaces
fillSpace()

# Letters that were previously entered
alreadyTyped = []

# hangman index
man = 6

# Chances
chance = 0

# Guess letter
guess = ''


# You wanna play? Let's play
play()