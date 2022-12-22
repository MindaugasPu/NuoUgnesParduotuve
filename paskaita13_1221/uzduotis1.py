# Turime logo su peršviečiamu fonu, dydis 128*128.
# Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir apačios
# nusiimtų po 28 eilutes pikselių. Išsisaugokite, nes naudosime
# sekančioms užduotims.

from PIL import Image

im = Image.open("logo.png")
new_im = im.crop((0, 28, 128, 100))
new_im.save("new_logo.png")


