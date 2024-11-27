import tkinter, random

w=500
h=500

canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

for i in range(10000):
    x=random.randint(5,w-15)
    y=random.randint(5,h-15)

    if x<w/2:       #lava       
        if y<h/2:       #lava hore
            if y>h/4 and x>h/4:     #cerna stvrt
                col="black"
            else:
                col="blue"
        else:       #lava dole
            if y<h/4*3 and x>h/4:       #cerna stvrt
                col="black"
            else:
                col="lime"
    else:       #prava
        if y<h/2:       #prava hore
            if x<h/4*3 and y>h/4:       #cerna stvrt
                col="black"
            else:
                col="red"
        else:       #prava dole
            if y<h/4*3 and x<h/4*3:         #cerna stvrt
                col="black"
            else:
                col="yellow"
    canvas.create_oval(x,y,x+10,y+10,fill=col)

tkinter.mainloop()