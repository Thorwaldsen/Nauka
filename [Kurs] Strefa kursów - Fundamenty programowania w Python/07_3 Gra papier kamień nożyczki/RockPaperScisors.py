import random


def rock_paper_scisors():
    options = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    info_string = "'R' for rock, 'P' for paper, 'S' for scissors"
    ai_pick = random.choice(list(options.keys()))
    user_pick = input(info_string).upper()

    while user_pick not in list(options.keys()):
        print("Invalid answer. Try again.")
        user_pick = input(info_string).upper()

    print("AI picked:", options[ai_pick], "|", "You picked:", options[user_pick])

    if (user_pick == 'P' and ai_pick == 'R') \
            or (user_pick == 'R' and ai_pick == 'S') \
            or (user_pick == 'S' and ai_pick == 'P'):
        print(options[user_pick], "beats", options[ai_pick])
        return "WINNER"
    elif user_pick != ai_pick:
        print(options[ai_pick], "beats", options[user_pick])
        return "LOOSER"
    else:
        return "TIE"


def play_again():
    return input("Do you want to play again? (Y/N) -> ").upper()


start = input("Do you want to start the game? (y/n)").upper()

while True:
    if start == "Y":
        game_result = rock_paper_scisors()
        if game_result == "WINNER":
            print("Congrats! You won.")
            start = play_again()
            continue
        elif game_result == "LOOSER":
            print("You lost.")
            start = play_again()
            continue
        else:
            print("Tie! Try again")
            continue
    elif start == "N":
        print("Maybe next time")
        break
    else:
        print("Invalid answer. try again")
        start = input("(Y/N) -> ").upper()
