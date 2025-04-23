subor=open("menaapriezv.txt","w", encoding="utf-8")
mena=open("mena.txt","r", encoding="utf-8")
priezviska=open("priezviska.txt","r", encoding="utf-8")

for name in mena:
    sname=priezviska.readline()
    print(f"{name.strip()} {sname.strip()}",file=subor)

mena.close()
priezviska.close()
