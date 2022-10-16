class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("Hau Hau!")

class Wolf(Dog):
    def howl(self):
        print("Jestem wilkiem,")
        super().voice()

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow!")

dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice()

print("\n")

cat = Cat("Burek", 8)
print(cat.name)
print(cat.age)
cat.getVoice()

print("\n")

wolf = Wolf("Przemek", 5)
print(wolf.name)
print(wolf.age)
wolf.howl()