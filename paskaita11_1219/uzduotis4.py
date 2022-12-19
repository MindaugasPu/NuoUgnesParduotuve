# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai:
#
# Naudoti sorted, attrgetter, reverse, funkciją repr
# from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"{self.vardas}, {self.amzius}")

zmogus1 = Zmogus("Mindaugas", 29)
zmogus2 = Zmogus("Ugnė", 30)

print(zmogus1)
print(zmogus2)

sarasas = [zmogus1, zmogus2]
print(sarasas)

print(sorted(sarasas, key= lambda x: x.amzius))
print(sorted(sarasas, key= lambda x: x.amzius, reverse=True))
print(sorted(sarasas, key=lambda x: x.vardas))
print(sorted(sarasas, key=lambda x: x.vardas, reverse=True))