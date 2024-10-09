n = int(input("zadaj n: "))
sucet=0
for i in range(n):
    sucet = sucet + (i+1) # sucet + (i+1) je vyraz, najskor sa vypocita vyraz a vysledna hodnota sa priradi do premennej sucet
    # print(i, i+1, sucet)
print("sucet prvych", n, "cisel je", sucet)