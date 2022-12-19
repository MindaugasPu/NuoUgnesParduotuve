# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# Sudėtų ir atspausdintų visus sąrašo žodžius
# Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
# Patarimai:
#
# Naudoti filter arba comprehension, sum, " ".join()

sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

suma = list(x for x in sarasas if type(x) is int or type(x) is float)
print(sum(list(suma)))

zodziai = list(x for x in sarasas if type(x) is str)
print(" ".join(zodziai))

print(sarasas.count(True))