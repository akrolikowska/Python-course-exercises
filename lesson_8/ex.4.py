import turtle
import random

def create_turtle(x,y):
    t = turtle.Turtle(shape="turtle",visible=False)
    t.color("green")
    t.penup()
    t.shapesize(5)
    t.setpos(x,y)
    t.showturtle()

scr = turtle.Screen()
scr.onscreenclick(create_turtle,1)
scr.listen()