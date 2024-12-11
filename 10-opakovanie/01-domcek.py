import tkinter
w=1500
h=800
canvas=tkinter.Canvas(width=w, height=h)
canvas.pack()

def haus(x,y,d,col):

    st=d/4
    #strecha
        # canvas.create_polygon(x0,y0,x1,y1,x2,y2)
    canvas.create_polygon(x,y+d/2,x+d,y+d/2,x+d/2,y)

    #fasada
    canvas.create_rectangle(x,y+d/2,x+d,y+d+d/2, fill=col)

    #okno
    canvas.create_rectangle(x+st,y+st*3,x+st*3,y+d+st, fill="#55ffff")
    canvas.create_line(x+d/2,y+st*3,x+d/2,y+d+st)
    canvas.create_line(x+st,y+d,x+st*3,y+d)

def ulica(x,y,d,pocet_dom):
    c1="#ff4600"
    c2="#ffff00"
    for i in range(pocet_dom):
        haus(x,y,d,c1)
        x+=d+10
        c1,c2=c2,c1

def dedina(d):
    y=10
    pocet_ul= h // (d + d // 2 + 10)
    pocet_dom= w // (d + 10)
    for i in range(pocet_ul):
        ulica(10,y,d,pocet_dom)
        y+=d/2*3+10

dedina(100)

tkinter.mainloop()

# def dedina(x,y,d,rd,sl):
#     for i in range(rd):
#         ulica(x,y,d,sl)
#         y+=d*2

# dedina(100,100,100,4,7)