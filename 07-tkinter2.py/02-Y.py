import tkinter
canvas=tkinter.Canvas()
canvas.pack()

f="#ff00ff"

def yps(x,y):
    
    #\
    canvas.create_rectangle(x,y,x+10,y+10, outline=f, fill=f)
    canvas.create_rectangle(x,y+10,x+10,y+20)
    canvas.create_rectangle(x+10,y+20,x+20,y+30)
    
    #/
    canvas.create_rectangle(x+40,y,x+50,y+10)
    canvas.create_rectangle(x+40,y+10,x+50,y+20)
    canvas.create_rectangle(x+30,y+20,x+40,y+30)

    #│
    canvas.create_rectangle(x+20,y+30,x+30,y+40)
    canvas.create_rectangle(x+20,y+40,x+30,y+50)
    canvas.create_rectangle(x+20,y+50,x+30,y+60)
    canvas.create_rectangle(x+20,y+60,x+30,y+70)

yps(10,10)


tkinter.mainloop()

