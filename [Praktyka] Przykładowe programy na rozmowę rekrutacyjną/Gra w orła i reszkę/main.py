# prosta gra w orła i reszkę. Użytkownik kontra komputer.
from random import randint
from time import sleep

throw = randint(0,1)
playerGuess = 1
computerGuess = randint(0,1)
validMode = True

# w przyszłości spróbować zamienić te funkcje w jedną
def playerOneThrows():
    if throw == 0:
        print("Heads")
    if throw == 1:
        print("Tails")

def playerTwoThrows():
    if throw == 0:
        print("Heads")
    if throw == 1:
        print("Tails")

def computerThrows():
    if throw == 0:
        print("Heads")
    if throw == 1:
        print("Tails")

def playerVsPlayer():
    print("Player vs Player")

def playerVsComputer():
    print("Player vs computer")

selectMode = input("Heads or Tails\nSelect game mode:\n1. Player vs Player\n2. Player vs computer\n")
gameMode = int(selectMode)


# zamienić tę pętlę w funkcję
while validMode:
    if gameMode == 1:
        playerVsPlayer()
        validMode = False
    elif gameMode == 2:
        playerVsComputer()
        validMode = False
    else:
        validMode = True
        gameMode = input("Select valid game mode\n")

