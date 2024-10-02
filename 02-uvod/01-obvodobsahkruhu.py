r = float(input("zadaj polomer: ")) # float je funkcia na prevod textu do des. cisla
# udajove typy: 
#   string - retazec znakov (text)
#   int - cele cisla
#   float - des. cisla
O = 2 * 3.14 * r     # desatinne cisla sa pisu s bodkou!!!
S = 3.14 * (r * r)
print("obvod kruhu je: ", round(O, 2)) # zaokruhlui cislo resp. premennu   O je premenna, 2 je pocet des. miest
print("obsah kruhu je: ", round(S, 2))
