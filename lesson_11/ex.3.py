import tkinter as tk
import tkinter.ttk as ttk
gui = tk.Tk()

gui.geometry("400x300")
button = tk.Button(gui, text="Click me").place(x=5,y=10)
checkbox = tk.Checkbutton(gui, text = "Accept this!").place(x=5,y=40)
label = tk.Label(gui, text="This is label").place(x=5,y=70)
slider = tk.Scale(gui, from_= 0, to=50).place(x=5,y=100)
radio1 = tk.Radiobutton(gui, text="Option 1", value="unchecked").place(x=5,y=130)
radio2 = tk.Radiobutton(gui, text="Option 2", value="unchecked").place(x=5,y=190)
entry = tk.Entry(gui).place(x=5, y=230)
spinbox = tk.Spinbox(gui, from_=0, to=10).place(x=5, y=260)


available_values = ["January", "February", "March", "April", "May", "June"]
combobox = ttk.Combobox(gui, values=available_values)
combobox.place(x=5,y=10)


gui.geometry("200x300")
for button_text in ["Button1", "Button2", "Button3"]:
    new_button = tk.Button(gui, text=button_text).pack()
