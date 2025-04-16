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