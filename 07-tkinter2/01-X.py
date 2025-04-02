import tkinter as tk
canvas=tk.Canvas(width=600, height=600)
canvas.pack()

def xko(x,y):      #definicia funkcie, "xko" je nazov (tp davame my), () su tzv parametre fcie

    #\
    canvas.create_rectangle(x,y,x+10,y+10, fill="black")
    canvas.create_rectangle(x,y+10,x+10,y+20, fill="black")
    canvas.create_rectangle(x+10,y+20,x+20,y+30, fill="black")
    canvas.create_rectangle(x+20,y+30,x+30,y+40, fill="black")
    canvas.create_rectangle(x+30,y+40,x+40,y+50, fill="black")
    canvas.create_rectangle(x+40,y+50,x+50,y+60, fill="black")
    canvas.create_rectangle(x+50,y+60,x+40,y+70, fill="black")

    #/
    canvas.create_rectangle(x+40,y,x+50,y+10, fill="black")
    canvas.create_rectangle(x+40,y+10,x+50,y+20, fill="black")
    canvas.create_rectangle(x+40,y+20,x+30,y+30, fill="black")
    #(stred)
    canvas.create_rectangle(x+20,y+40,x+10,y+50, fill="black")
    canvas.create_rectangle(x+10,y+50,x,y+60, fill="black")
    canvas.create_rectangle(x,y+60,x+10,y+70, fill="black")

def riadok_x(x,y,pocet):
    for i in range(pocet):
        xko(x,y)
        x+=60

def riadky_x(x,y,pocet_riadkov, pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_x(x,y,pocet_stlpcov)
        y+=100

xko(10,10)
riadok_x(10,100,6)
riadky_x(10,190,2,7)

# xko(10,10)       volanie fcie, na tomto mieste sa vykona
# xko(70,10)
# xko(130,10)

# x=10
# y=10
# for i in range(3):
#     pocet=5
#     for i in range(pocet):
#         xko(x,y)
#         x=x+60
#     x=10
#     y=y+80

tk.mainloop()