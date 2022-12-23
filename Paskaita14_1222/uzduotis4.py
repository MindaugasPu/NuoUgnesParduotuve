# Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių,
# kuriuos reikia jame išcenzūruoti sąrašą. Pvz, žodis "kvaraba" yra baisus
# keiksmažodis, ir mums reikia duotame tekste pakeisti k*****a. Pradėkite maždaug taip:
# # iškvietus funkciją
# # mums atspausdintų
# # baisūs žodžiai, tokie kaip k*****a, ž****s..
# žodžių cenzūravimui naudokite regex, o jų sukeitimui tekste naudokite .replace()\
import re


def cenzura(tekstas, *keiksmai):
    pattern = re.compile(r'([a-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])')
    for x in keiksmai:
        paieska = pattern.search(x)
        print(paieska)
        dalis = len(paieska.group(2)) * '*'
        keitimas = pattern.sub(f'\g<1>{dalis}\g<3>', x)
        tekstas = tekstas.replace(x, keitimas)
    print(tekstas)

cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')

