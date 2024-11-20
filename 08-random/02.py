import random, tkinter

s=int(input("zadaj veklost stvorca: "))
pocet=int(input("zadaj pocet stvorcov: "))

canvas=tkinter.Canvas(height=400,width=400)
canvas.pack()


for i in range(pocet):
    x=random.randint(3,500-s-3)
    y=random.randint(3,400-s-3)
    canvas.create_rectangle(x,y,x+s,y+s,fill=random.choice(["red","blue","green","yellow","magenta","cyan"]))

tkinter.mainloop()