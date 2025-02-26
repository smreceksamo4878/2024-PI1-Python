# range(od, do -1, krok)
# range moze mat aj klesjucu postupnost range(5, 0, -1) 
print(list(range(1, 5, 2)))

ret="ahoj"
for i in range(len(ret)):
    print(ret[-i-1])
print()

for i in range(len(ret)-1, -1, -1):
    print(ret[i])