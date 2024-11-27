import tkinter, random

w=int(input("sirka platna: "))
h=int(input("vyska platna: "))

canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

for i in range(1000):
    x=random.randint(5,w-15)
    y=random.randint(5,h-15)
    
    # if x<w/2 and y<h/2:
    #     col="blue"
    # elif x<w/2 and y>h/2:
    #     col="yellow"
    # elif x>w/2 and y<h/2:
    #     col="#20ff20"
    # elif x>w/2 and y>h/2:
    #     col="red"

    if x<w/2:
        if y<h/2:
            col="blue"
        else:
            col="lime"
    else:
        if y<h/2:
            col="red"
        else:
            col="yellow"
    canvas.create_oval(x,y,x+10,y+10,fill=col)

tkinter.mainloop()