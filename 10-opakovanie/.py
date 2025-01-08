import tkinter
import random

def vypis():
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y,
                       text=vstup.get(),
                       font=f'arial {velkost.get()}',
                       fill=farba.get())

def zmaz():
    canvas.delete('all')

canvas = tkinter.Canvas()
canvas.pack(side='left')
tkinter.Button(text='Vypíš text', command=vypis).pack()
tkinter.Button(text='Zmaž plochu', command=zmaz).pack()
tkinter.Label(text='Zadaj text:').pack()
vstup = tkinter.Entry(width=10)
vstup.pack()
tkinter.Label(text='Zadaj farbu:').pack()
farba = tkinter.Entry(width=10)
farba.pack()
tkinter.Label(text='Zmeň veľkosť:').pack()
velkost = tkinter.Scale(orient='horizontal', from_=10, to=40, length=75)
velkost.pack()

tkinter.mainloop()