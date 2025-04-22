<<<<<<< HEAD
import tkinter, random

karty=list("A B C D E F G H".split())*2
random.shuffle(karty)

tlacitka=[]
odhalene=[]
zhoda=[]

def odhal(i,j):
    index=i*4+j
    
=======
import tkinter,random

def vytvor_karty():
    karty=list(range(1,9))*2
    random.shuffle(karty)
    return(karty)

canvas=tkinter.Canvas()
for i in range(16):
    tlacitko=tkinter.Button( width=10, height=3 command= )
    tlacitko.grid()
>>>>>>> 9403ed0a0edb27c7ab2f1375d96b7354c76fcba7
