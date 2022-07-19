import turtle
canvas = tk.Canvas(gui, width=100, height=,
canvas.pack()
t = turtle.RawTurtle(canvas)

def go_forward():
    t.porward(100)
button = tk.Button(gui, text="Forward", command=go+forward)
button.pack()