import tkinter
canvas=tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(20,10,30,20)
canvas.create_rectangle(30,20,40,10, fill="black")
canvas.create_rectangle(10,30,20,40, fill="black")
