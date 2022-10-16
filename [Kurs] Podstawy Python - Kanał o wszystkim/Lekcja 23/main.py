def decorator(func):
    def wrapper():
        print("\n------------")
        func()
        print("------------\n")
    return wrapper

def hello():
    print("Hello World!")

hello2 = decorator(hello)
hello2()

@decorator
def witaj():
    print("Witaj Świecie!")

witaj()

hello()