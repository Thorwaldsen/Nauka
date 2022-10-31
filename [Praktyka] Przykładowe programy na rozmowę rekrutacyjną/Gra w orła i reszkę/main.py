# prosta gra w orła i reszkę. Użytkownik kontra komputer.
from random import randint
from time import sleep

playerPoints = 0
computerPoints = 0
end = True

def delay():
    for i in range(3):
        print(i+1, end="")
        sleep(0.2)
        for j in range(3):
            print(".", end="")
            sleep(0.25)
        print("\n", end="")

def throws():
    global playerPoints
    throw = randint(1, 2)
    decision = input("Your turn. Type:\n1. Heads\n2. Tails\n")
    decisionInt = int(decision)
    print("Your type:", throw)
    #    delay()
    if throw == decisionInt:
        print("You guesed:", throw)
        playerPoints += 1
        print("Your points:", playerPoints)
        print("Computer points:", computerPoints,"\n")
        del throw
    else:
        print("You didn't guessed", throw)
        print("Your points:", playerPoints)
        print("Computer points:", computerPoints,"\n")
        del throw

def computerThrows():
    global computerPoints
    computerChoise = randint(1, 2)
    throw = randint(1, 2)
    print("Computer's turn")
    print("Computer's type:", computerChoise)
    if throw == computerChoise:
        print("Computer guessed:", throw)
        computerPoints += 1
        print("Computer points:", computerPoints)
        print("Your points:", playerPoints,"\n")
        del throw
    else:
        print("Computer didn't guessed", throw)
        print("Computer points:", computerPoints)
        print("Your points:", playerPoints,"\n")
        del throw

def mainMenu():
    input("Welcome to Heads or Tails\nPress enter to continue\n")
    global end
    while end:
        if playerPoints != 3 and computerPoints != 3:
            throws()
            computerThrows()
        elif (playerPoints == 3 and computerPoints != 3) or (playerPoints != 3 and computerPoints == 3):
            end = False
            if playerPoints > computerPoints:
                print("Wygrałeś!")
            else:
                print("Przegrałeś!")

mainMenu()