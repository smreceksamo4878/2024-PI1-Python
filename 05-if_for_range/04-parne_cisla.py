cislo=int(input("zadaj cislo: "))

#vypis parnych cisel
print(f"parne cisla do {cislo}:")
for i in range(2,cislo+1,2):
    print(i)

#vypis neparnych cisel1
print(f"neparne cisla do {cislo}:")
for i in range(1,cislo+1,2):
    print(i)

if (cislo%2 == 0):
    print("cislo je parne")
else:
    print("cislo je neparne")