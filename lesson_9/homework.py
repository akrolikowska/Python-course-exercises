import turtle

t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)

t = turtle.Turtle()

sides = [100,200,100,200]
for side in sides:
    t.forward(side)
    t.left(90)


t.forward(75)
t.left(120)
t.forward(150)
t.left(120)
t.forward(150)
t.left(120)
t.forward(75)
'''
n = int(input("How many angles: "))
inner_angle = (n - 2) * 180 // n
for x in range(n):
    t.forward(150)
    t.left(180 - inner_angle)