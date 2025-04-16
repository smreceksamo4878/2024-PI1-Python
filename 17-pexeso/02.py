import tkinter,random

def vytvor_karty():
    karty=list(range(1,9))*2
    random.shuffle(karty)
    return(karty)

canvas=tkinter.Canvas()
for i in range(16):
    tlacitko=tkinter.Button( width=10, height=3 command= )
    tlacitko.grid()