import tkinter,random

file = open("data.txt", "w")
pism=random.choice("ORL")
x1=random.randint(3,797)
y1=random.randint(3,797)
x2=random.randint(3,797)
y2=random.randint(3,797)
c1=random.randint(0,255)
c2=random.randint(0,255)
c3=random.randint(0,255)

print(pism,x1,y1,x2,y2,c1,c2,c3, file=file)

file.close()

canvas = tkinter .Canvas(width=800, height=800)
canvas.pack()

with open("data.txt", "r") as file:
    riadky = [riadok.strip() for riadok in file if riadok.strip()]

for r in riadky:
    riadok = r.split(" ")

    if riadok[0] == "R": canvas.create_rectangle(riadok[1], riadok[2], riadok[3], riadok[4], 
                                                 fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
    elif riadok[0] == "O": canvas.create_oval(riadok[1], riadok[2], riadok[3], riadok[4], 
                                              fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
    else: canvas.create_line(riadok[1],riadok[2], riadok[3], riadok[4], 
                                  fill=f"#{int(riadok[5]):02x}{int(riadok[6]):02x}{int(riadok[7]):02x}")
        
canvas.mainloop()