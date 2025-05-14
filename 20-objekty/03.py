from random import choice, randint

class auto:
    def __init__(self, znacka, rok, farba):
        self.znacka = znacka 
        self.rok = rok
        self.farba = farba

    def info(self):
        print(f"Som {self.znacka} vyrobena v roku {self.rok} a moja farba je {self.farba}")

for i in range(10):      
    print("                       ")
    car=auto(choice(["skoda", "audi", "vw", "bmw", "lada "]), 
            randint(1980,2018), 
            choice(["modra", "zelena", "biela", "cierna", "ruzova", ]))
    car.info()
    
print("                       ")