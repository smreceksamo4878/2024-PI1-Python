teploty=[10,13,15,20]
print(teploty[0])

nakup=["chlieb","maslo","mlieko"]
print(nakup[2])

zviera=["pes","Dunco",2020,"hneda",10.7] #do listu mozeme ukladat hodnoty roznych typov (int, str, bool...)
print(zviera)
print(zviera[2])

#v pythone su listy dynamicke - nemusia mat definovanu velkost
#prvky pridavame fciou append()
prazdny=[]
print(prazdny)
prazdny.append(25)
print(prazdny)
prazdny.append("ahoj")
print(prazdny)
prazdny.append(100)
print(prazdny[-1])

#listy vieme aj zretazit (spocitat)
nakupazviera=nakup+zviera
print(nakupazviera)

print("Dunco" in zviera)

#narozdiel od stringov su listy menitelne
prazdny[0]=1000
print(prazdny)