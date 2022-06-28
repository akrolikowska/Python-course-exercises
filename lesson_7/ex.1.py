class Rectangle:
    a = 0
    b = 0

    def area(self):
        return self.a * self.b
    def perimeter(self):
        return 2*self.a + 2*self.b
    def print_name(self):
        print("Prostokat")

rect = Rectangle()
rect.a = 5
rect.b = 10
print(rect.a, rect.b)

x = rect.area()

y = rect. perimeter()
print(x,y)