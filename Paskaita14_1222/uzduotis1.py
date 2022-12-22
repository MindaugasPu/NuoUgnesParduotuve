# parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy)
# keistų į yyyy mm dd. Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.

import re

def reformavimas(data):
    pattern = re.compile(r'(\d{2}).(\d{2}).(\d{4})')
    rezultatas = pattern.search((data))
    print(f"{rezultatas.group(3)} {rezultatas.group(2)} {rezultatas.group(1)}")


reformavimas("12.22.2022")