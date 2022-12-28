
class Tankas:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kryptis = 'Š'
        self.sove = 0
        self.registras = {'Š': 0, 'P': 0, 'V': 0, 'R': 0}
    def pirmyn(self):
        self.kryptis = 'Š'
        self.y += 1
        return self.y

    def atgal(self):
        self.kryptis = 'P'
        self.y -= 1
        return self.y

    def kairen(self):
        self.kryptis = 'V'
        self.x -= 1
        return self.x

    def desinen(self):
        self.kryptis = 'R'
        self.x += 1
        return self.x

    def suvis(self):
        self.sove += 1
        self.registras[self.kryptis] += 1
        return self.sove, self.registras

    def info(self):
        print(f'Tanko padėtis - x:{self.x} y:{self.y}, kryptis į {self.kryptis} || Bendras šūvių skaičius: {self.sove} - {self.registras}')


tankas = Tankas()

while True:
    print()
    tankas.info()
    match (input('''"w" - važiuoti Šiaurės kryptimi,
"s" - važiuoti Pietų kryptimi,
"a" - važiuoti Vakarų kryptimi,
"d" - važiuoti Rytų kryptimi,
"f" - ŠŪVIS!
"l" - baigti žaidimą.
Jūsų veiksmas:''')):
        case 'w':
            tankas.pirmyn()
        case 'a':
            tankas.kairen()
        case 's':
            tankas.atgal()
        case 'd':
            tankas.desinen()
        case 'f':
            tankas.suvis()
        case 'l':
            print("Žaidimo pabaiga")
            break
        case _:
            print("Klaidinga įvestis. Bandykite dar kartą!")



