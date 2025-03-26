ret="Ahoj Svet"
ret1=ret[:4]
ret2=ret[5:]
print(ret1)
print(ret2)
# ret[5]="s" - toto nie je dovolene v pythone 
nret=ret[:5] + "s" + ret[6:]
print(nret)
nret=nret + " svet"
print(nret)
nret= 3*(nret + " ")
print(nret)