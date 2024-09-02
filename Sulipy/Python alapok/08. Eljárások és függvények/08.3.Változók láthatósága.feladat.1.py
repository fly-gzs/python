'''
Írj egy programot, amely generál egy véletlenszámot [1; 10] intervallumon,
és a játékosnak ezt kell kitalálnia. A próbálkozások száma nincs megkötve,
de a program számolja a tippelési alkalmakat.

A program tartalmazzon
egy kitalalando nevű változót, ebben kerüljön tárolásra a generált véltelenszám,
egy tipp nevű változót, ez tárolja az éppen aktuális tippet,
egy main nevű függvényt, amely tartalmazza a főprogramot,
egy eltalalta nevű függvényt, amelynek
- 2 paramétere van, a játékos éppen aktuális tippje és az kitalálandó szám,
- visszatérési értéke True vagy False, attól függően,
hogy a paraméterként átvett értékek megegyeznek-e egymással vagy nem,
egy tipp_bekero nevű függvényt, amelynek
- nincs paramétere,
- bekéri a felhasználó tippjét, és azzal tér vissza.
'''

def eltalalta(a,b):
    ertek = False
    if a != b:
        print(f'Nem találtad el. Ez volt a {szamlalo} próbálkozásod.')
    else:
        print(f'Gratulálok eltaláltad {szamlalo} próbálkozásból!')
        print('Játék vége!')
        ertek = True
    return ertek

def tipp_bekero():
    tipp = 0
    global szamlalo
    szamlalo = 0
    kitalalando = random.randint(1,10)
#     print(kitalalando)
    while tipp != kitalalando:
        tipp = int(input('Tippelj! '))
        szamlalo += 1
        eltalalta(kitalalando,tipp)
    return tipp

import random

def main():
    print('Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!')
    tipp_bekero()
    
main()

