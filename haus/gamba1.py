import math 
import random
s=int(input("zadaj vstupnu cenu: "))
n=int(input("zadaj cislo od 1 do 8: "))
nahodme = random.randint(1, 8)
if 1<n<8:
    if (n == nahodme):
        print("vyhral si! novy zostatok: ", s * 2)

    else:
        print("smola! :c novy zostatok: ", s/2, )
else:
    print("si retard? mas zadat cislo od 1 do 8")
    