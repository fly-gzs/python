'''
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt,
amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat
tárolja el a program egy listában, és ezt értékelje ki a függvény!
(Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
'''

def harommal_oszthatok(lista):
    szamlalo = 0
    for szam in lista:
        if szam % 3 == 0:
            szamlalo += 1
    return szamlalo

lista = []
be_szam = 0
while be_szam >= 0:
    be_szam = int(input('Adj meg egy pozitív számot: '))
    if be_szam >= 0:
        lista.append(be_szam)

print(harommal_oszthatok(lista))