import random
from DiceFaceDiagram import DiceFaceDiagram


def parse_input(input_string):
    if input_string.strip() in {'1', '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        exit()


def roll_dice(n_dice):
    roll_results = []
    for _ in range(n_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


n_dice_input = input("How many dice do you want to roll? [1-6] -> ")
n_dice = parse_input(n_dice_input)

roll_result = roll_dice(n_dice)

dice_face_diagram = DiceFaceDiagram(roll_results=roll_result)

dice_face_diagram.display_results()