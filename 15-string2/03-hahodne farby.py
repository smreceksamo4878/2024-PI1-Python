import tkinter, random
canvas=tkinter.Canvas(width=800,height=600)
canvas.pack()

for i in range(10):
    x=random.randint(3,750)
    y=random.randint(3,550)
    canvas.create_rectangle(x,y,x+50,y+50,fill=f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}" )

canvas.mainloop()