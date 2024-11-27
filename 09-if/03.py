import tkinter, random

w=500
h=500

canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

for i in range(10000):
    x=random.randint(5,w-15)
    y=random.randint(5,h-15)

    if x<w/2:
        if y<h/2:
            if y>h/4 and x>h/4:
                col="black"
            else:
                col="blue"
        else:
            if y<h/4*3 and x>h/4:
                col="black"
            else:
                col="lime"
    else:
        if x<h/4*3 and y<h/4: # desi tu je chyba
            if y<h/4:
                col="black"
            else:
                col="red"
        else:
            if y<h/4*3 and x<h/4*3:
                col="black"
            else:
                col="yellow"
    canvas.create_oval(x,y,x+10,y+10,fill=col)

tkinter.mainloop()