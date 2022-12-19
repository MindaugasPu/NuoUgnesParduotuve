# Sukurtų sąrašą iš skaičių nuo 0 iki 50
# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų. Šį sąrašą (list masyvą) priskirti naujam kintamajam.
# Su kvadratų sąrašu (nauju kintamuoju) atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai

from statistics import mean, median

sarasas = list(range(51))
padaugintas = [x * 10 for x in sarasas]
dalinasi = [y for y in sarasas if y % 7 == 0]
dalinasi2 = list(filter(lambda y2: y2 % 7 == 0, sarasas))
kvadratu = [x ** 2 for x in sarasas]


print(sarasas)
print(padaugintas)
print(dalinasi)
print(dalinasi2)
print(kvadratu)
print(min(kvadratu), max(kvadratu), sum(kvadratu), mean(kvadratu), median(kvadratu))
print(sorted(kvadratu, reverse=True))