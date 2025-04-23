import tkinter, random

karty=list("A B C D E F G H".split())*2
random.shuffle(karty)

tlacitka=[]
odhalene=[]
zhoda=[]

def odhal(i,j):
    index=i*4+j
