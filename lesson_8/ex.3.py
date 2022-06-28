import turtle
import random

for i in range(10):
    t.forward(x)
    t.penup()
    t.forward(x)
    t.pendown()


def go_forward():
    t.forward(100)

t = turtle.Turtle()
scr = turtle.Screen()

t = turtle.Turtle()
scr.onkey(go_forward, "space")
scr.listen()


def go_forward():
    t.forward(100)
def go_back():
    t.backward(100)
def left():
    t.left(90)
def right():
    t.right(90)

t = turtle.Turtle()
scr = turtle.Screen()

t = turtle.Turtle()
scr.onkey(go_forward, "w")
scr.onkey(go_back, "s")
scr.onkey(left, "a")
scr.onkey(right, "d")
scr.listen()