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