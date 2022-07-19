import tkinter as tk
gui = tk.Tk()

entries = {}

for i in ["Name", "Adress", "City"]:
    frame = tk.Frame(gui)
    label = tk.Label(frame, text=i)
    entry = tk.Entry(frame)
    entries[i.lower()] = entry
    label.pack(side=tk.LEFT)
    entry.pack(side=tk.RIGHT)
    frame.pack ()

def add_user():
    name=entries["name"].get()
    adress=entries["adress"].get()
    city=["city"].get()
    if name and adress and city:
        with open("data.txt", "a") as datafile:
            datafile.write( ";".join([name, adress, city]) + "\n")

button = tk.Button(gui, text="Add user", command=add_user)
button.pack()