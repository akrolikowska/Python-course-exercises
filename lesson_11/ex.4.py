label = tk.Label(gui, text="Initial text", bg="red")
label.pack()

def button_pressed():
    label.config(text="CHANGED!", bg="green")
new_button = tk.Button(gui, text="Change label", command=button_pressed).pack(fill=tk.X)


label = tk.Label(gui, text="Value 0")
label.pack()

def slider_changed(value):
    label.config(text="Value: " + str(value))

slider = tk.Scale(gui, from_=-10, to=10, command=slider_changed)
slider.pack()


login_frame = tk.Frame(gui)
login_label = tk.Label(login_frame, text="Login")
login_entry = tk.Entry(login_frame)
login_label.pack(side=tk.LEFT)
login_entry.pack(side=tk.RIGHT)
login_frame.pack()

password_frame = tk.Frame(gui)
password_label = tk.Label(password_frame, text="Pasword")
password_entry = tk.Entry(password_frame, show="*")
password_label.pack(side=tk.LEFT)
password_entry.pack(side=tk.RIGHT)
password_frame.pack()

users = {}

def add_user():
    login=login_entry.get()
    password=password_entry.get()
    if not login in users.keys():
        users[login] = password
        print("Add user: " + login + " " + users[login])
    else:
        print("User" + login + "already exist")

button = tk.Button(gui, text="OK, please login", command=add_user)
button.pack()