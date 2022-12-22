# sukurkite funkciją, kuri priimtų
# paveikslėlį
# kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes
# išsaugoti ar ne reikšmę
# ir atitinkamai pakoreguotų paveikslėlio nustatymus.
# Parodytų nuotrauką ekrane. Priklausomai nuo pasirinkimo,
# išsaugotų arba ne. Išsaugokite faile, prie originalaus pavadinimo
# pridėję pvz. '_modified', tarkime dog_modified.jpg.

from PIL import Image, ImageEnhance

# pavadinimas = input("Įveskite atidaromo paveikslėlio pavadinimą: ")
# def paveikslelis():
#     im = Image.open(f"{pavadinimas}")
#     return im
# def kontrastas():
#     kontrastas = ImageEnhance.Contrast(paveikslelis())
#     pasirinkimas1 = "n"
#     a1 = "1"
#     while True:
#         if pasirinkimas1 == "y":
#             kontrastas.enhance(a1).save(f'{pavadinimas[0:-4]}_modified.jpg')
#             break
#         else:
#             a1 = float(input("Įveskite kontrasto reikšmę (0-20)"))
#             kontrastas.enhance(a1).show()
#             pasirinkimas1 = input("Ar kontrastas tinkamas? y/n:")

def nuotraukos_redagavimas(nuotrauka, kontrastas, spalvingumas, astrumas, sviesumas, issaugoti=False):
    im = Image.open(nuotrauka)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(kontrastas)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(spalvingumas)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(astrumas)
    enh = ImageEnhance.Brightness(im)
    im = enh.enhance(sviesumas)
    if issaugoti:
        im.save(nuotrauka[0:-4]+"_modified"+nuotrauka[-4])
    im.show()

nuotraukos_redagavimas('dog.jpg', 2, 0, 5, 1, True)



