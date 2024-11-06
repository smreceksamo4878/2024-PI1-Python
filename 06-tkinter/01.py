import tkinter

canvas= tkinter.Canvas()    #vytvorenie platna a jeho priradenie do premennej canvas
canvas.pack()   #umiestneni platna do okna 

canvas.create_text(100,75, text="ahoj")    #vypise text "ahoj" na pozicii x=100 y=100
canvas.create_rectangle(50,50,150,100)      #prve 2 pociatocny bod      #dalsie 2 konecny bod
canvas.create_oval(50,50,150,100)     #vykreslenie kruhu/ovalu      #tie iste parametre ako stvorec  


tkinter.mainloop()  #aby zostalo okno otvorene