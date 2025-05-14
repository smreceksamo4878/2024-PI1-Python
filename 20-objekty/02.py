class zviera:
    def __init__(self,meno):
        self.meno = meno

    def predstav_sa(self):
        print(f"ja som {self.meno}")

class macka(zviera):
    def miauci(self):
        print(f"som {self.meno} a hovorim miau")

class pes(zviera):
    def steka(self):
        print(f"som {self.meno} a robim hau")

dino=pes("dino")
micka=macka("micka")

dino.predstav_sa()
dino.steka()

micka.predstav_sa()
micka.miauci()