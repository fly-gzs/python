'''
Készíts egy programot, amely generál és listában tárol 10 darab véletlenszámot
[-20; 20] inetrvallumon, kírja a lista elemeit,
majd megjeleníti azokat növekvő sorrendben is!
A lista rendezését saját magad által megírt algoritmus végezze
beszúró rendezés módszerével!
  
'''

import random
szamok = []
szamlalo = 1
while szamlalo <= 10:
    random_szam = random.randint(1,10)
    szamok.append(random_szam)
    szamlalo += 1
print(szamok)

for i in range(1,len(szamok)):
    j = i-1
    while j >= 0 and szamok[j] > szamok [j+1]:
        szamok[j], szamok[j+1] = szamok[j+1], szamok[j]
        j = j-1
    
print(szamok)
        