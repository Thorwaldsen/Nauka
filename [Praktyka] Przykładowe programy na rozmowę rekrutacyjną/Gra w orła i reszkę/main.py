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
    global end
    throw = randint(1, 2)
    decision = input("Your type:\n1. Heads\n2. Tails\n")
    decisionInt = int(decision)
    #    delay()
    print(throw)
    if throw == decisionInt:
        print("You guesed:", throw)
        playerPoints += 1
        print("Your points:", playerPoints)
        del throw
        if playerPoints == 3:
            return 0
        throws()
    else:
        print("You didn't guessed", throw)
        print("Your points:", playerPoints)
        del throw
        throws()

throws()
