import math 
import random

v=int(input("zadaj vklad: "))
n=int(input("zadaj cislo od 1 do 8: "))

rng = random.randint(1, 8)
if 1<n<8:
    if (n == rng):
        s=v*4
        print("vyhral si! novy zostatok: ", s)
    else:
        s=v/2
        print("smola! :c novy zostatok: ", s)
else:
    print("si jelito? mas zadat cislo od 1 do 8")
