class Ingredients:
    def __init__(self, name, protein, carbon, fat):
        self.name = name
        self.protein = protein
        self.carbon = carbon
        self.fat = fat


class Meals:
    def __init__(self, name):
        self.name = name

    def add_ingredient(self, weight, ingredient):
        self.weight = weight
        self.ingredient = ingredient


class DayProgram:
    def add_meals(self, meal):
        self.meal = meal


egg = Ingredients("Egg", 13, 1.1, 11)
tomato = Ingredients("Tomato", 0.9, 3.9, 1)
bread = Ingredients("Bread", 9, 49, 3.2)

scrambled_eggs = Meals("Scrambled eggs")
scrambled_eggs.add_ingredient(200, egg)
scrambled_eggs.add_ingredient(50, tomato)

sandwich = Meals("Sandwich")
sandwich.add_ingredient(25, bread)
sandwich.add_ingredient(50, tomato)

very_minimalistic_menu = DayProgram()
very_minimalistic_menu.add_meals(scrambled_eggs)
very_minimalistic_menu.add_meals(sandwich)
