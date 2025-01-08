import tkinter
canvas=tkinter.Canvas()
canvas.pack()

def vytlac():
    label.config(text=textbox.get())

label=tkinter.Label()
label.pack()

textbox=tkinter.Entry()
textbox.pack()

button=tkinter.Button(text="vytlac", command=vytlac)
button.pack()

tkinter.mainloop()