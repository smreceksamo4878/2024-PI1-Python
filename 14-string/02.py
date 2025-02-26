slovo=input("zadaj slovo: ")
d=len(slovo)

print("dlzka retazca je", d,"znakov")
print()

for i in slovo:
    print(i)
print()

for j in range(len(slovo)):
    print(slovo[-j-1])
print()

for k in slovo:
    print(k*3)
