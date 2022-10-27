# prosta gra w orła i reszkę. Użytkownik kontra komputer.
from random import randint
from time import sleep

throw = randint(0,1)
playerGuess = 1
computerGuess = randint(0,1)
computerPoints = 0

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
    playerOnePoints = 0
    playerTwoPoints = 0

    while playerOnePoints != 3 or playerTwoPoints != 3:
        playerOneThrows()
        decision = input("Player vs Player\n[Player 1] Select:\n1. Heads\n2. Tails\n")
        decisionInt = int(decision)
        if throw == decisionInt:
            print("nie zgadłeś")
            playerOnePoints =+ 0
            print("Player one points = ", playerOnePoints, "Player two points = ", playerTwoPoints)
        else:
            print("zgadłeś")
            playerOnePoints =+ 1
            print("Player one points = ", playerOnePoints, "\nPlayer two points = ", playerTwoPoints)

def playerVsComputer():
    print("Player vs computer")

def mainMenu(mode):
    validMode = True
    while validMode:
        if mode == 1:
            playerVsPlayer()
            validMode = False
        elif mode == 2:
            playerVsComputer()
            validMode = False
        else:
            validMode = True
            gameMode = input("Select valid game mode\n")


selectMode = input("Heads or Tails\nSelect game mode:\n1. Player vs Player\n2. Player vs computer\n")
gameMode = int(selectMode)
mainMenu(gameMode)
