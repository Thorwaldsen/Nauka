from abc import ABC
from abc import abstractmethod


class DuckBehaviour(ABC):

    @abstractmethod
    def fly(self):
        print("I'm flying")

    @abstractmethod
    def say(self):
        print("Quack, quack!")

    @abstractmethod
    def go_to(self):
        print("I'm going like a duck")


class Duck(DuckBehaviour):
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()


class Toy:
    def __init__(self, material, color):
        self.color = color
        self.material = material


class DuckToy(Toy, DuckBehaviour):
    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()
