import tkinter, random

st=int(input("zadaj pocet stvorcov: "))
w=int(input("sirka platna: "))
h=int(input("vyska platna: "))

canvas=tkinter.Canvas(width=w,height=h)
canvas.pack()

for i in range(st):
    s=random.randrange(1,30)
    x=random.randint(5,w-5-s)
    y=random.randint(5,h-5-s)
    if s<10:
        farba="red"
    elif s<20:
        farba="#22ff22"
    else:
        farba="blue"
    canvas.create_rectangle(x,y,x+s,y+s,fill=farba)

tkinter.mainloop()