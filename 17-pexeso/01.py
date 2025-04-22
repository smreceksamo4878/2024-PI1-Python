<<<<<<< HEAD
import tkinter as tk
import random

# Hlavné premenné
karty = list("A B C D E F G H".split()) * 2
random.shuffle(karty)

tlacitka = []
odhalene = []
zhoda = []

# Funkcia na odhalenie karty
def odhal(i, j):
    index = i * 4 + j

    if index in zhoda or index in odhalene:
        return

    tlacitka[i][j]['text'] = karty[index]
    odhalene.append(index)

    if len(odhalene) == 2:
        root.after(1000, over_zh)

# Funkcia na overenie zhody
def over_zh():
    global odhalene, zhoda
    i1, j1 = divmod(odhalene[0], 4)
    i2, j2 = divmod(odhalene[1], 4)

    s1 = karty[odhalene[0]]
    s2 = karty[odhalene[1]]

    if s1 == s2:
        zhoda += odhalene
    else:
        tlacitka[i1][j1]['text'] = "?"
        tlacitka[i2][j2]['text'] = "?"

    odhalene = []

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("4x4 Pexeso")

# Vytvorenie mriežky tlačidiel
for i in range(4):
    row = []
    for j in range(4):
        btn = tk.Button(root, text="?", width=6, height=3, command=lambda i=i, j=j: odhal(i, j))
        btn.grid(row=i, column=j)
        row.append(btn)
    tlacitka.append(row)

root.mainloop()
=======
import tkinter, random

def vytvor_karty():
    karty=list(range(1,9))*2
    random.shuffle(karty)
    return karty

def kliknutie(index):
    global prva_karta
    if odkryte[index]:
        return
    
    odkryte[index] = True
    tlacitka[index].config(text=str(karty[index]))

    if prva_karta is None:
        prva_karta = index
    else:
        if karty[prva_karta] == karty[index]:
            print("Pár nájdený!")
        else:
            root.after(500, zakryj_karty, prva_karta, index)
        prva_karta = None

# Funkcia na zakrytie kariet
def zakryj_karty(prva_karta, druha_karta):
    odkryte[prva_karta] = False
    odkryte[druha_karta] = False
    tlacitka[prva_karta].config(text="")
    tlacitka[druha_karta].config(text="")

# Vytvorenie okna
root = tkinter.Tk()
root.title("Pexeso 4x4")

# Rámec pre tlačidlá
frame = tkinter.Frame(root)
frame.pack()

# Zoznam tlačidiel a kariet
karty = vytvor_karty()
odkryte = [False] * 16
tlacitka = []

# Prvá karta
prva_karta = None

# Vytvoríme tlačidlá
for i in range(16):
    tlacitko = tkinter.Button(frame, width=10, height=3, command=lambda i=i: kliknutie(i))
    tlacitko.grid(row=i // 4, column=i % 4)
    tlacitka.append(tlacitko)

# Spustíme hlavný cyklus
root.mainloop()
>>>>>>> 9403ed0a0edb27c7ab2f1375d96b7354c76fcba7
