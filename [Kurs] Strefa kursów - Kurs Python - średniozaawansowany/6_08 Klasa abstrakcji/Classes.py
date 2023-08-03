from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    def __init__(self):
        raise Exception("Unable to create object of abstract class")

    def print_information(self):
        pass

    @abstractmethod
    def give_voice(self):
        raise NotImplementedError()


class Mammal(Animal):
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def go_to(self):
        print("Going to places")

    def print_information(self):
        print(self.name)
        print(self.age)
        Animal.print_information(self)
        print("I, am a mammal")


class Boy(Mammal):
    def __init__(self, age, name, surname):
        Mammal.__init__(self, age, name)
        self.surname = surname

    def give_voice(self):
        print("Little boy wants to play")

    def print_information(self):
        Mammal.print_information(self)
        print(self.surname)
        print("I am a boy")
