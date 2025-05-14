class Auto:
    def __init__(self, znacka):
        self.znacka = znacka  # atribút objektu

    def predstav_sa(self):
        print(f"Som auto značky {self.znacka}")

moje_auto = Auto("Škoda")
moje_auto.predstav_sa()