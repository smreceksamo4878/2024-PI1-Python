import tkinter, random
canvas=tkinter.Canvas()
canvas.pack()

cis=random.randint(0,9)

textbox=tkinter.Entry()
textbox.pack()

i=1

def hra():
    cisloM=int(textbox.get())
    global i
    if cisloM < cis:
        label.config(text="dal si mensie")
        i=+1
    elif cisloM > cis:
        label.config(text="dal si vecsie")
        i+=1
    else:
        i+=1
        label.config(text=f"uhadol si na {i} pokusov")
    

button=tkinter.Button(text="skus :)",command=hra)
button.pack()

label=tkinter.Label()
label.pack()

tkinter.mainloop()