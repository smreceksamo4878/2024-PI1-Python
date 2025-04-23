subor=open("subor.txt","r")    # "subor.txt" je relativna cesta, subor musi byt v tom istom priecinku ako kod
# otvori txt subor na citanie, pre zapis sa pouziva "w"
# subor=open("c:/dokumenty/subor.txt","r") - absolutna cesta "c:/dokumenty/subor.txt"
# subor=open("¨../16-list/subor.txt","r") - .. je o priecinok vyssie

# for i in range(4):
#     riadok=subor.readline() # readline precita cely riadok zo suboru a ulozi do premennej
#     print(riadok)

# riadok=subor.readline()
# while riadok != "":
#     riadok=subor.readline()

while True:
    riadok=subor.readline()
    if riadok=="":
        break
    print(riadok.strip())