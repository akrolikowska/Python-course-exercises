canvas = tk.Canvas(gui, width=500, height=400)
canvas.create_rectangle(10,10,50,100, fill="red")
canvas.create_polygon(100,100,150,20,70,100, fill="blue")
canvas.create_oval(100,150,50,200, fill="green")

img = tk.PhotoImage(file="corgi_icon.png")
canvas.create_image(200,250, image=img)
canvas.pack()