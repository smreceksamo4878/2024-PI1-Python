print("oliver + niki = janko \n")

import datetime

class Osoba:    #triedy vzdy zaciame velkym pismwnom

    def __init__(self, meno, priezvisko, rok):    #konstruktor, zavola sa pri vzniku obj.
        self.meno = meno    #atribut - vlastnost
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self):    #metoda - co vie obj. robit
        print(f"ahoj, ja som {self.meno} {self.priezvisko} a mam {self.vek} rokov")

    def vypis_meno(self):
        print(self.meno, self.priezvisko)

    def vypis_vek(self):
        print(self.vek)

    def vypis_rok(self):
        print(self.rok)    

class Student(Osoba):   #trieda 
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok) #to super znamena ze pouzije atributy z rodicovskej triedy (Osoba)
       #Osoba.__init__(meno, priezvisko, rok)
        self.trieda = trieda

    def pozdrav(self):
        super().pozdrav()
        print(f"som z {self.trieda} triedy")
        #polymorfizmus - menime metodu pozdrav z rodicovskej triedy

# samo=Osoba("samo", "smrecek", 2008)    #vznikne obj. samo, vytvoreny pomocou classy Osoba
# samo.pozdrav()    #volame metodu obj. pozdrav
# fero=Osoba("oliver", "veselka", 2008)
# fero.pozdrav()

# fero.vypis_meno()
# fero.vypis_rok()
# fero.vypis_vek()

student = Student("kubo", "vrskoviskockokosskokovsky", 2008, "1.AT")
student.pozdrav()

