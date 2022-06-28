import turtle
import random

n = int(input("How many angles: "))
inner_angle = (n-2)*180//n
for x in range(n):
    t.forward(150)
    t.left(180-inner_angle)


t.begin_fill("brown")
t.circle(80)
t.color("red")
t.begin_fill("brown")


t.fillcolor("brown")
t.begin_fill()
t.forward(20)
t.right(90)
t.forward(200)
t.right(90)
t.forward(40)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.end_fill()
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()


shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
colors = ["yellow", "red", "blue", "orange", "pink", "black", "green", "purple"]

for i in range(10):
    t = turtle.Turtle()
    t.pensize(3)
    t.shapesize(2)
    t.color(random.choice(colors))
    t.shape(random.choice(shapes))
    t.left(random.randint(1,360))
    t.forward(random.randint(30,350))


stefan = turtle.Turtle()
basia = turtle.Turtle()
kasia = turtle.Turtle()

stefan.shape("turtle")
stefan.color("red")
stefan.forward(100)

kasia.shape("classic")
kasia.color("yellow")
kasia.backward(200)


t = turtle.Turtle()
x = 20
t.pensize(3)