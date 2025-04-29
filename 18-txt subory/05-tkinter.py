import tkinter

canvas=tkinter.Canvas()
canvas.pack()

fbody=open("body.txt","r")

for bod in fbody:
    print(bod)
    medz=bod.find(" ")
    x=int(bod[:medz])
    y=int(bod[medz+1:])
    print(x)
    print(y)
    canvas.create_oval(x-5,y-5,x+5,y+5)
    

tkinter.mainloop()