# stringv py je immutable - nezmenitelny
ret="ahoj svet"
# ret[0]="b" - toto nie je mozne
ret="j" + ret[1:] # ak chceme zmenit znak, treba takto
print(ret)

# retazce vieme porovnavat 

print("a" == "a")
print("a" > "A")
print(ord("a")) # ord() je funkcia, kt vrati ciselnu hodnotuv znaku
print(ord("A"))
print(chr(64)) # chr() je fcia, kt. na zaklade ordinalnej hodnoty vrati znak