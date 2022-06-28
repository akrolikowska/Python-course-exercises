class Rectangle(KlasaRodzic):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

rect = Rectangle(5,10)
print(rect.area())

rect1 = Rectangle(99,1850)
print(rect1.area())

rect_small = Rectangle(0.6, 0.03)
print(rect_small.area())

class Rectangle(KlasaRodzic):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
