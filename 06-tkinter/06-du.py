import tkinter
canvas=tkinter.Canvas()
canvas.pack()

#S
canvas.create_rectangle(20,10,30,20, outline="#ffaa00", fill="#ffaa00")
canvas.create_rectangle(30,20,40,10, outline="#ff5500", fill="#ff5500")
canvas.create_rectangle(40,10,50,20, outline="#ff0000", fill="#ff0000")
canvas.create_rectangle(50,20,60,10, outline="#ff0055", fill="#ff0055")
canvas.create_rectangle(10,20,20,30, outline="#ffff00", fill="#ffff00")
canvas.create_rectangle(20,30,10,40, outline="#aaff00", fill="#aaff00")
canvas.create_rectangle(20,40,30,50, outline="#55ff00", fill="#55ff00")
canvas.create_rectangle(30,50,40,40, outline="#00ff00", fill="#00ff00")
canvas.create_rectangle(40,40,50,50, outline="#00ff55", fill="#00ff55")
canvas.create_rectangle(50,50,60,60, outline="#00ffaa", fill="#00ffaa")
canvas.create_rectangle(60,60,50,70, outline="#00ffff", fill="#00ffff")
canvas.create_rectangle(50,70,40,80, outline="#00aaff", fill="#00aaff")
canvas.create_rectangle(40,80,30,70, outline="#0055ff", fill="#0055ff")
canvas.create_rectangle(30,70,20,80, outline="#0000ff", fill="#0000ff")
canvas.create_rectangle(20,80,10,70, outline="#5500ff", fill="#5500ff")

#A vrch
canvas.create_rectangle(100,10,110,20, outline="#ff5500", fill="#ff5500")
canvas.create_rectangle(110,20,120,10, outline="#ff0000", fill="#ff0000")
canvas.create_rectangle(120,10,130,20, outline="#ff0055", fill="#ff0055")
#A lava
canvas.create_rectangle(100,20,90,30, outline="#ffaa00", fill="#ffaa00")
canvas.create_rectangle(100,40,90,30, outline="#ffff00", fill="#ffff00")
canvas.create_rectangle(100,40,90,50, outline="#aaff00", fill="#aaff00")
canvas.create_rectangle(100,60,90,50, outline="#55ff00", fill="#55ff00")
canvas.create_rectangle(100,60,90,70, outline="#00ff00", fill="#00ff00")
canvas.create_rectangle(100,80,90,70, outline="#00ff55", fill="#00ff55")
#A prava
canvas.create_rectangle(130,20,140,30, outline="#ff00aa", fill="#ff00aa")
canvas.create_rectangle(130,40,140,30, outline="#ff00ff", fill="#ff00ff")
canvas.create_rectangle(130,40,140,50, outline="#aa00ff", fill="#aa00ff")
canvas.create_rectangle(130,60,140,50, outline="#5500ff", fill="#5500ff")
canvas.create_rectangle(130,60,140,70, outline="#0000ff", fill="#0000ff")
canvas.create_rectangle(130,80,140,70, outline="#5500ff", fill="#5500ff")
#A stred
canvas.create_rectangle(100,40,110,50, outline="#55ff55", fill="#55ff55")
canvas.create_rectangle(120,40,110,50, outline="#00aaaa", fill="#00aaaa")
canvas.create_rectangle(120,40,130,50, outline="#5555ff", fill="#5555ff")
tkinter.mainloop()