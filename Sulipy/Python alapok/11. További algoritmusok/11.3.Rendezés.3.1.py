'''
Készíts egy programot, amely generál és listában tárol 10 darab véletlenszámot
[-20; 20] inetrvallumon, kírja a lista elemeit,
majd megjeleníti azokat növekvő sorrendben is!
A lista rendezését saját magad által megírt algoritmus végezze
buborék rendezés módszerével! Ezen a honlapon tudod megnézni a
buborékrendezés működését és pszeudókódját.
  
'''

import random
szamok = []
szamlalo = 1
while szamlalo <= 10:
    random_szam = random.randint(1,10)
    szamok.append(random_szam)
    szamlalo += 1
print(szamok)

for index in range(len(szamok)-1,-1,-1):
    for x in range(0, index-1):
        if szamok[x] > szamok[x+1]:
            szamok[x], szamok[x+1] = szamok[x+1], szamok[x]
print(szamok)
        