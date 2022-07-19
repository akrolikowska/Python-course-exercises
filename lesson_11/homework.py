import tkinter as tk
gui = tk.Tk()

#ex.1

entries = {} # słownik, który przechowuje obiekty do okienek "Entry", pozostałe obiekty nie będą potem
#potrzebne

for i in ["Name","Address","City"]:
    frame = tk.Frame(gui)
    label = tk.Label(frame, text=i)
    entry = tk.Entry(frame)
    entries[i.lower()] = entry
    label.pack(side=tk.LEFT)
    entry.pack(side=tk.RIGHT)
    frame.pack()

def add_user():
    name=entries["name"].get()
    address=entries["address"].get()
    city=entries["city"].get()

    if name and address and city:
        with open("data.txt", "a") as datafile:
            datafile.write( ";".join([name, address, city]) + "\n" )

button = tk.Button(gui, text="Add user", command=add_user)
button.pack()

#ex.2

scales = {}
for i in ["Red", "Green", "Blue"]:
    frame = tk.Frame(gui)
    label = tk.Label(frame, text=i, fg=i)
    scale = tk.Scale(frame, from_=0, to=255, orient="horizontal")
    scales[i[0]] = scale
    label.pack()
    scale.pack(side=tk.RIGHT)
    frame.pack()

canvas = tk.Canvas(gui, width=200, height=200, bg="black")
canvas.pack()

def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def showcolor():
    r = scales["R"].get()
    g = scales["G"].get()
    b = scales["B"].get()
    canvas.config(bg=from_rgb((r,g,b)))

button = tk.Button(text="Show!", command=showcolor)
button.pack()

#ex.3

import tkinter as tk
import tkinter.ttk as ttk
import random

gui = tk.Tk()
available_figures = ["Square", "Rectangle", "Circle", "Ellipse"]
combo = ttk.Combobox(gui, values=available_figures)
combo.pack()

button = tk.Button(text = "Choose figure")
button.pack()

scales = {}
labels = {}

for i in [1,2]:
    frame = tk.Frame(gui)
    label = tk.Label(frame, text=str(i))
    labels[i] = label
    scale = tk.Scale(frame, from_=0, to=255, orient="horizontal")
    scales[i] = scale
    label.pack(side=tk.LEFT)
    scale.pack(side=tk.RIGHT)
    frame.pack()

def set_labels_and_scales():
    figure = combo.get()
    if figure == "Square" or figure == "Circle":
        labels[1].config(state="normal")
        scales[1].config(state="normal")
        labels[2].config(state="disabled")
        scales[2].config(state="disabled")
        labels[1].config(text = "a" if figure == "Square" else "r" )
    elif figure == "Rectangle" or figure == "Ellipse":
        labels[1].config(state="normal")
        scales[1].config(state="normal")
        labels[2].config(state="normal")
        scales[2].config(state="normal")
        labels[1].config(text="a")
        labels[2].config(text="b")

button.config(command=set_labels_and_scales)

available_colors = ["red", "yellow", "green", "blue", "pink", "purple", "black"]
colorcombo = ttk.Combobox(gui, values=available_colors)
colorcombo.pack()

canvas = tk.Canvas(gui, width=400, height=400, bg="white")
canvas.pack()

def drawfigure():
    figure = combo.get()
    x0=random.randint(0,400)
    y0=random.randint(0,400)
    if figure == "Square":
        a = scales[1].get()
        canvas.create_rectangle(x0,y0,x0+a,y0+a, fill=colorcombo.get())
    elif figure == "Rectangle":
        a = scales[1].get()
        b = scales[2].get()
        canvas.create_rectangle(x0,y0,x0+a,y0+b, fill=colorcombo.get())
    elif figure == "Circle":
        r = scales[1].get()
        canvas.create_oval(x0-r,y0-r,x0+r,y0+r, fill=colorcombo.get())
    elif figure == "Ellipse":
        a = scales[1].get()
        b = scales[2].get()
        canvas.create_oval(x0-a,y0-b,x0+a,y0+b, fill=colorcombo.get())

button = tk.Button(text="Draw!", command=drawfigure)
button.pack()


