import tkinter
import random
bezi = bezi1 = True

def kresli():
    x = random.randint(10, 370)
    y = random.randint(10, 250)
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')
    if bezi:
        canvas.after(100, kresli)

def kresli1():
    x = random.randint(10, 370)
    y = random.randint(10, 250)
    canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill='blue')
    if bezi1:
        canvas.after(300, kresli1)

def prvy():
    global bezi
    bezi = not bezi
    if bezi:
        kresli()
def druhy():
    global bezi1
    bezi1 = not bezi1
    if bezi1:
        kresli1()

def zmaz():
    canvas.delete('all')

canvas = tkinter.Canvas()
canvas.pack(side='left')
tkinter.Button(text='Prvý proces', command=prvy).pack()
tkinter.Button(text='Druhý proces', command=druhy).pack()
tkinter.Button(text='Zmaž plochu', command=zmaz).pack()

kresli()
kresli1()

tkinter.mainloop()