class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is" + str(self.name) + str(self.age) + "and I am a dog")
    def sound(self):
        print("Default sound!")

class Dog(Animal):
    def sound(self):
        print("wof wof")

class Cat(Animal):
    def sound(self):
        print("meow meow")

snake = Animal("Python", 30)
dog = Dog("Goldi", 2)
cat = Cat("Mruczek", 5)

print(snake.name, dog.name, cat.name)
snake.sound()
dog.sound()
cat.sound()