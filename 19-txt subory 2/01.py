import tkinter,random   

canvas=tkinter.Canvas(width=800, height=800)
canvas.pack()

subor=open("tvary.txt", "w")

riadok=[]

tvar=random.choice("orl")
riadok.append(tvar)

for i in range(8):
    for i in range(4):
        suradnice=random.randint(3,797)
        riadok.append(suradnice)

    for i in range(3):
        farba=random.randint(0,255)
        riadok.append(farba)

    print(riadok,file=subor)
    
# tkinter.mainloop()