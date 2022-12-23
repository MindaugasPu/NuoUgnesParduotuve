# Atspausdinkite tą patį teksta taip:
#
# # 1.
# # Event: Workshop & Tutorial proposals due
# # Date: November 21, 2019
#
# # 2.
# # Event: Notification of acceptance
# # Date: December 1, 2019
#
# # ir t.t.

import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

def datos():
    pattern = re.compile(r'\w+\s\d{2},\s\d{4}$', re.M)
    rezultatas1 = pattern.findall(text)
    return rezultatas1

def iki_dvitaskio():
    pattern = re.compile(r'^[A-Za-z0-9\s&\-()]*', re.M)
    rezultatas2 = pattern.findall(text)
    return rezultatas2

for x in range(len(text.splitlines())):
    print(f'{x}.\nEvent: {iki_dvitaskio()[x-1]}\nDate: {datos()[x-1]}\n')

