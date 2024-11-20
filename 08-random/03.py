import random, tkinter

pocet=int(input("zadaj pocet jednotek: "))

canvas=tkinter.Canvas(height=400,width=500)
canvas.pack()

def jedn(x,y):
    
    canvas.create_rectangle(x,y+10,x+10,y+20,fill=random.choice(["red","yellow","blue"]))

    canvas.create_rectangle(x+10,y,x+20,y+10,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+10,x+20,y+20,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+20,x+20,y+30,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+30,x+20,y+40,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+40,x+20,y+50,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+50,x+20,y+60,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+10,y+60,x+20,y+70,fill=random.choice(["red","yellow","blue"]))

    canvas.create_rectangle(x,y+60,x+10,y+70,fill=random.choice(["red","yellow","blue"]))
    canvas.create_rectangle(x+20,y+60,x+30,y+70,fill=random.choice(["red","yellow","blue"]))

for i in range(pocet):
    jedn(random.randint(3,467),random.randint(3,327))

tkinter.mainloop()