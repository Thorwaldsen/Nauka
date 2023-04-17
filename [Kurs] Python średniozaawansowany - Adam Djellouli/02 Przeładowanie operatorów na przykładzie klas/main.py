# klasa reprezentująca wektor 2D (x,y)

class Wektor:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    def __isadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


wektor1 = Wektor(6, 2)
wektor2 = Wektor(4, 8)
wektor3 = wektor1 + wektor2
wektor3 += wektor2

print(wektor1.x)
print(wektor1.y)
print(wektor2.x)
print(wektor2.y)
print(wektor3.x)
print(wektor3.y)
