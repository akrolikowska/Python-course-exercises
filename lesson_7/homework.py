#ex.1

class Snake:
    def  __init__(self, colour, size):
        self.colour = colour
        self.size = size
        self.poison = False

    def sss(self):
        print("sss")

    def introduce(self):
        print("My name is snake and my colour is " + self.colour)

    def info(self):
        print("My size is " + self.size)
        if self.poison == True:
            print("Uwaga gryzę i umrzesz! ")
        else:
            print("spoko, przeżyjesz")

snake1 = Snake("green", "XL")
snake1.sss()
snake1.introduce()
snake1.info()

#ex.2

class Fridge:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
        self.icemachine = False

    def alarm(self):
        print("Doors are open!")

    def ice(self):
        if self.ice == True:
            print("Mogę zrobić Ci lód do drinka!")
        else:
            print("Sorry, musisz zam zadbać o zmrożenie wody do drineczków...")

    def info(self):
        print("My brand is " + self.brand)

fridge1 = Fridge("Samsung", "black")
fridge1.alarm()
fridge1.ice()
fridge1.info()

#ex.3

class Employee():
    name = ""
    age = 0
    salary = 0

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def increase_salary(self, amount):
        self.salary +=amount

pawel = Employee()
pawel.name = "Paweł"
pawel.age = 29
pawel.salary = 10000
print(pawel.get_name())
print(pawel.get_salary())
pawel.increase_salary(2000)
print(pawel.get_salary())

#ex.3

class Monster:
    name = ""
    power = 0
    is_aggresive = False

    def say_hello(self):
        print("Hello I am " + self.name + " and I can kill you")

    def attack(self, hero):
        if is_aggresive:
            hero.hp -= self.power
        return hero.hp

    def regenerate(self, hp):
        self.power += hp

vampire = Monster()
vampire.name = "Mietek"
vampire.power = 50
vampire.is_aggresive = False
vampire.say_hello()
my_hero = Hero()
my_hero.hp = vampire.attack(my_hero)
vampire.regenerate(100)

class Hero:
    name = ""
    race_type = ""
    position = 0
    hp = 0

    def say_hello(self):
        print("Hello, my name is " + self.name + " and I am " + self.race_type)

    def go(self, new_position):
        self.position + new_position

    def fight(self, enemy_power):
        if enemy_power > self.hp:
            self.hp -=int(0.5*enemy_power)

my_hero = Hero()
my_hero.name = "Hulk"
my_hero.race_type = "Green evil"
my_hero.hp = 200
my_hero.say_hello()
my_hero.go(100)
print(my_hero.position)
print(my_hero.hp)
my_hero.fight(30)
print(my_hero.hp)
my_hero.fight(120)
print(my_hero.hp)

'''
#ex.4

class Turtle:
    def  __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.x = 0

    def say_name(self):
        print("Hi I am turtle " + self.name)

    def move(self):
        self.x = self.x + self.speed

    def get_position(self):
        return self.x

turtle1 = Turtle("Franklin", 10)
turtle1.move()
turtle1.get_position()
print(turtle1.x)

#ex.5

class Book:
    def __init__(self, author, tittle, pages):
        self.author = author
        self.tittle = tittle
        self.pages = pages
        self.current_page = 0

    def print_book(self):
        print(self.tittle + " written by " + self.author + " has " + str(self.pages) + " pages")

    def goto_page(self, page):
        if page < self.pages:
            self.current_page = page
        else:
            self.current_page = self.pages

    def get_current_page(self):
        return self.current_page

book1 = Book("Mille", "Winnie the Pooh", 120)
book1.print_book()
book1.goto_page(69)
print(book1.get_current_page())

#ex.6

class Bird:
    def __init__(self, species, colour, size, origin):
        self.species = species
        self.colour = colour
        self.size = size
        self.origin = origin
        self.wings = 2
        self.position = 0

    def get_position(self):
        return self.position

    def get_species(self):
        return self.species

    def get_colour(self):
        return self.colour

    def get_size(self):
        return self.size

    def geg_origin(self):
        return self.origin

    def get_wings(self):
        return self.wings

    def fly(self):
        print("Fru fru")

    def poop(self):
        print(" sru sru plask na człowieka")

    def move(self):
        self.position = self.position + km

class Pingwin(Bird):
    def __init__(self, species, colour, size, origin, partner):
        super().__init__(species, colour, size, origin)
        self.partner = partner

    def fly(self):
        print("sorry ja nie latam ")

pingwin1 = Pingwin("Cesarski", "Black and White", "small", "Arctic", "always")
pingwin1.poop()
pingwin1.fly()


#ex.7

#czlowiek - pracownik - ksiegowy
class Employee:
    def __init__(self, name, age, profession, experience):
        self.name = name
        self.age = age
        self.proffesion = profession
        self.experience = experience

    def introduce(self):
        print("Hello my name is " + self.name + " and I am " + self.age + " years old")

    def jump(self):
        print("jump jump jump!")

    def go_workout(self):
        print("Czas na siłke!")

class Fire_fighter(Employee):
    def __init__(self, name, age, profession, experience, tall, efficiency):
        super().__init__(name, age, profession, experience)
        self.tall = tall
        self.efficiency = efficiency

    def go_to_fire(self):
        print("Czas ruszać do pożaru!")

człowiek1 = Fire_fighter("Piotr", "30", "strażak", "5 lat doświadczenia", "185 cm", "bardzo sprawny" )
człowiek1.introduce()
człowiek1.go_workout()
człowiek1.go_to_fire()



#postac-wojownik-ninja

class Fighter:
    def __init__(self, power, regenerate, name):
        self.power = power
        self.regenerate = regenerate
        self.name = name

    def attack(self):
        return(self.power + 50)

    def introduce(self):
        print("Hello, my name is " + self.name)

class Ninja:
    def __init__(self, power, regenerate, name, position, species):
        super().__init__(self, power, regenerate, name)
        self.position = position
        self.species = species

    def go(self):
        return(self.position + 50)

warior1 = Ninja("speed", "200", "Jackie_Chan", 30, "killer"
warior1.attack()
warior1.introduce()
warior1.go()

#ex.8

import math
#math.sqrt(N)
class Rectangle:
    def __init__(self, bok1, bok2):
        self.bok1 = bok1
        self.bok2 = bok2

    def bok_a(self):
        print(self.bok1)

    def bok_b(self):
        print(self.bok2)

    def area(self):
        return(self.bok1 * self.bok2)

class Square:
    def __init__(self, bok1, bok2, colour):
        super().__init__(self, bok1, bok2)
        self.colour = colour

    def kolor(self):
        print(self.colour)

figura = Square(10, 15, "czerwony")
figura.bok_a()
figura.bok_b()
figura.area()
figura.kolor()
    

#ex.9 

import math

class Figure:
    def print_name(self):
        print(self.__class__.__name__)

class Triangle(Figure):
    def __init__(self, single_side, double_side):
        if not (single_side > 0 and double_side > 0):
            raise ValueError
        self.a = single_side
        self.b = double_side
        self.c = double_side

    def perimeter(self):
        return self.a + self.b + self.c

    def field(self):
        h = math.sqrt(self.b**2 - (0.5*self.a)**2)
        return(self.a * h)/2

class Rectangle(Figure):
    def __init__(self, a_side, b_side):
        if not (a_side > 0 and b_side >0):
            raise ValueError
        self.a = a_side
        self.b = b_side

    def perimeter(self):
        return 2*self.a + 2*self.b

    def field(self):
        return self.a*self.b

class Circle(Figure):
    def __init__(self,radius):
        if not radius > 0:
            raise ValueError
        self.r = radius

    def perimeter(self):
        return 2*math.pi*self.r

    def field(self):
        return math.pi * self.r**2

triangle = Triangle(3,5)
rectangle = Rectangle(3,5)
circle = Circle(3)
tab = [triangle, rectangle, circle]

for fig in tab:
    fig.print_name()
    print("Field: " + str(fig.field()) + ", perimeter:" + str(fig.perimeter()))
















