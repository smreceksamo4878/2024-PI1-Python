fo=input("zadaj hex farby obrysu : " )
fv=input("zadaj hex farby vyplne : " )
s=int(input("zadaj velkost stvorceka v pixeloch: "))

import tkinter
canvas=tkinter.Canvas(height=500, width=500)
canvas.pack()

def yps(x,y):
    
    #\
    canvas.create_rectangle(x,y,x+s,y+s, outline=fo, fill=fv)
    canvas.create_rectangle(x,y+s,x+s,y+s*2, outline=fo, fill=fv)
    canvas.create_rectangle(x+s,y+s*2,x+s*2,y+s*3, outline=fo, fill=fv)
    
    #/
    canvas.create_rectangle(x+s*4,y,x+s*5,y+s, outline=fo, fill=fv)
    canvas.create_rectangle(x+s*4,y+s,x+s*5,y+s*2, outline=fo, fill=fv)
    canvas.create_rectangle(x+s*3,y+s*2,x+s*4,y+s*3, outline=fo, fill=fv)

    #│
    canvas.create_rectangle(x+s*2,y+s*3,x+s*3,y+s*4, outline=fo, fill=fv)
    canvas.create_rectangle(x+s*2,y+s*4,x+s*3,y+s*5, outline=fo, fill=fv)
    canvas.create_rectangle(x+s*2,y+s*5,x+s*3,y+s*6, outline=fo, fill=fv)
    canvas.create_rectangle(x+s*2,y+s*6,x+s*3,y+s*7, outline=fo, fill=fv)


yps(10,10)

tkinter.mainloop()