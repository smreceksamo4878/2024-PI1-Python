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
def gamba():
    g=s
    m=int(input("zadaj cislo od 1 do 8: "))
    rng = random.randint(1, 8)
    if 1<m<8:
        if (m == rng):
            s=s*4
            print("vyhral si! novy zostatok: ", s)
        else:
            s=s/2
            print("smola! :c novy zostatok: ", s)
    else:
            print("si jelito? mas zadat cislo od 1 do 8")
yn=int(input("chces pokracovat? 1 ak ano, 2 ak nie: "))
while yn==1:
    gamba()
else:
    print("fbjkd")