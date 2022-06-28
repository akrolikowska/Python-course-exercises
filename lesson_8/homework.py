import turtle

#ex.1
import turtle

a=turtle.Turtle()
a.up()
a.backward(50)
a.right(90)
a.forward(100)
a.left(90)
a.down()
a.fillcolor("BLUE")
a.begin_fill()

#ex.2

for x in range(5):
    a.forward(200)
    a.left(180-108)
a.end_fill()
a.hideturtle()

b=turtle.Turtle()
b.color("WHITE")
b.begin_fill()
for i in [100,50,100,50]:
    b.forward(i)
    b.right(90)
b.end_fill()
b.hideturtle()

c = turtle.Turtle()
c.up()
c.forward(45)
c.down()
c.color("RED")
c.begin_fill()
for i in [10,50,10,50]:
    c.forward(i)
    c.right(90)
c.end_fill()
c.hideturtle()

d = turtle.Turtle()
d.up()
d.right(90)
d.forward(20)
d.down()
d.color("RED")
d.begin_fill()

for i in [10,100,10,100]:
    d.forward(i)
    d.left(90)
d.end_fill()
d.hideturtle()

#ex.3
coder = turtle.Turtle()
for i in range(5):
    coder.forward(100)
    coder.left(72)

coder = turtle.Turtle()
for i in range(4):
    coder.forward(50)
    coder.left(90)
    coder.forward(50)
    coder.right(90)

t = turtle.Turtle()

#ex.4

point = 6
star_angle = 360.0/point
left_angle = star_angle * 2
side = 100

for k in range(point):
    t.forward(side)
    t.right(star_angle)
    t.forward(side)
    t.left(left_angle)


t = turtle.Turtle()
m = 1

for i in range(100):
    t.forward(m+i)
    t.right(m*15)

t = turtle.Turtle()

#ex.5

side_a = 300
side_b = 200

for i in [side_a,side_b,side_a,side_b]:
    t.penup()
    t.forward(0.1*i)
    t.pendown()
    t.forward(0.8*i)
    t.penup()
    t.forward(0.1*i)
    t.pendown()
    t.left(90)

#ex.6
import turtle
import math
import random

scr = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.left(90)
step = 100
colors = ["red", "blue", "green", "pink", "black", "orange"]

def up():
    y0 = t.ycor()
    t.sety(y0 + step)

def down():
    y0 = t.ycor()
    t.sety(y0 - step)

def left():
    x0 = t.xcor()
    t.setx(x0 - step)

def right():
    x0 = t.xcor()
    t.setx(x0 + step)

def up_left():
    x0 = t.xcor()
    y0 = t.ycor()
    t.goto(x0 - 0.5*step*math.sqrt(2), y0 + 0.5*step*math.sqrt(2))

def down_left():
    x0 = t.xcor()
    y0 = t.ycor()
    t.goto(x0 - 0.5*step*math.sqrt(2), y0 - 0.5*step*math.sqrt(2))

def up_right():
    x0 = t.xcor()
    y0 = t.ycor()
    t.goto(x0 + 0.5*step*math.sqrt(2), y0 + 0.5*step*math.sqrt(2))

def down_right():
    x0 = t.xcor()
    y0 = t.ycor()
    t.goto(x0 + 0.5*step*math.sqrt(2), y0 - 0.5*step*math.sqrt(2))

def change_color():
    t.color( random.choice(colors) )

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

def size_up(x,y):
    w,h,o = t.shapesize()
    t.shapesize(1.2*w, 1.2*h)

def size_down(x,y):
    w,h,o = t.shapesize()
    t.shapesize(0.8*w, 0.8*h)

scr.onkey(up, "8")
scr.onkey(down, "2")
scr.onkey(left, "4")
scr.onkey(right, "6")
scr.onkey(up_left, "7")
scr.onkey(down_left, "1")
scr.onkey(up_right, "9")
scr.onkey(down_right, "3")
scr.onkey(change_color, "5")
scr.onkey(toggle_pen, "0")
scr.onscreenclick(size_up, 3)
scr.onscreenclick(size_down, 1)
scr.listen()

turtle.mainloop()


