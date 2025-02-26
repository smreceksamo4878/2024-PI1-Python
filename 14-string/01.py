#string je retazec znakov
#retazec zaciname a koncime "" alebo ''
#\n - novy riadok, \t - tabulator, \" - vypise uvodzovky
#funkcia len() - vrati dlzku retazca (pocet znakov)
#znaky v retazci su indexovane - prvy znak ma index 0, index piseme do []

retazec = "ahoj svet"
print(retazec)
print(len(retazec))
print(retazec[5])

for i in range(len(retazec)):
    print(retazec[i])
    
for znak in retazec:
    print(znak)