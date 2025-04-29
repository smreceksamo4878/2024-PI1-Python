import tkinter

canvas=tkinter.Canvas(width=500, height=500)
canvas.pack()

subor=open("body.txt")


# for i in range(3):
#     tvar=subor.readline()
#     if tvar=="o":
#         canvas.create_oval(x)


for i in range(4):
    tvar=subor.readline()
    farba=subor.readline()
    coord=subor.readline()
    medz=coord.find(" ")
    x=int(coord[:medz])
    y=int(coord[medz+1:])
    if tvar.strip()=="o":
        canvas.create_oval(x-5,y-5,x+5,y+5, fill=farba.strip())
    if tvar.strip()=="r":
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill=farba.strip())
                         
tkinter.mainloop()


